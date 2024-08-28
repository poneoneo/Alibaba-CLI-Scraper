"""This script is responsible for scraping data from the Alibaba website.
It uses the Playwright library to navigate through multiple pages
extract HTML content,and save it to disk. The script defines
functions to handle asynchronous tasks,interact with
browser contexts, and gather data from the scraped HTML files.
Additionally, it utilizes loguru for logging purposes and decouple for
managing environment variables.
"""

import asyncio
import os
import time
from asyncio import TaskGroup
from typing import Optional

import playwright
import playwright.sync_api
import urllib3
from click import UsageError
from loguru import logger
from playwright.async_api import BrowserContext, async_playwright
from playwright.async_api import Page as AsyncPage
from playwright.sync_api import Error as PError
from playwright.sync_api import sync_playwright
from rich import print as rprint
from rich.progress import (
	Progress,
	SpinnerColumn,
	TaskID,
)

from . import SBR_WS_CDP_LIST
from .html_to_disk import write_to_disk
from .info_message import run_scrapper_with_success

HTML_PAGE_RESULT = []


async def goto_task(
	url: str,
	context_browser: BrowserContext,
	task: TaskID,
	progress: Progress,
	semaphore: asyncio.Semaphore,
	tg_instance: TaskGroup,
	page: AsyncPage,
	page_results: int,
) -> Optional[str]:
	"""Get HTML content from a URL.

	This function will load a page from a given URL,
	get its HTML content and save it to a global list.
	It will also update a progress bar with the task ID.

	Parameters:
		url (str): The URL of the page to be loaded.
		context_browser (BrowserContext): The browser context to be used.
		task (TaskID): The task ID of the current task.
		progress (Progress): The progress bar to be updated.
		semaphore (asyncio.Semaphore): The semaphore to be used to limit the number of concurrent tasks.
		tg_instance (TaskGroup): The task group instance.
		page (AsyncPage): The page object to be used.
		page_results (int): The number of pages to be scrapped.

	Returns:
		Optional[str]: The HTML content of the page if successful, otherwise None.
	"""
	try:
		async with page:
			logger.info(f"Loading page {url.split('page=')[1]} ... ")
			response = await page.goto(url, wait_until="domcontentloaded", timeout=0)
			if response is None:
				return None
			logger.info(f"get response text from web page {url.split('page=')[1]} ... ")
			html_body = await response.text()
			progress.start_task(task)
			progress.update(task, advance=100 / page_results)
			global HTML_PAGE_RESULT
			HTML_PAGE_RESULT.append(html_body)
			logger.info(f"Closing page {url.split('page=')[1]} ... ")
	except Exception as e:
		logger.error(f"Error processing page {url.split('page=')[1]}: {e}")
		return None


def urls_pusher(words: str, stop_at: int):
	for i in range(1, stop_at + 1):
		yield f"https://www.alibaba.com/trade/search?spm=a2700.galleryofferlist.0.0.64271d1dZRDxt1&fsb=y&IndexArea=product_en&keywords={words}&tab=all&&page={i}"


@logger.catch()
async def async_scrapper(*, save_in: str, key_words: str, page_results: int) -> None:
	"""
	Initiates scraping of Alibaba.com based on the provided keywords.

	:param save_in: The directory to store the raw HTML files.
	:type save_in: str
	:param key_words: The search term(s) for finding products on Alibaba. Enclose multiple keywords in quotes.
	:type key_words: str
	:param page_results: The number of pages to scrape. If omitted, 10 pages will be scraped.
	:type page_results: int

	:return: None
	:rtype: None

	:raises UsageError: If no internet connection is available.

	:raises SystemExit: If the Bright data account has been suspended by the system.

	:raises SystemExit: If no SCRAPING BROWSER API key is provided.

	:raises playwright._impl._errors.Error: If there is an error with the playwright browser.

	:raises Exception: If there is an error processing a page.
	"""
	async with async_playwright() as p:
		logger.info("Connecting to CDP and creating the browser... ")
		try:
			api_key = SBR_WS_CDP_LIST
			if api_key == "":
				rprint(
					"[red]You need to set your SCRAPING BROWSER API key from BrightData to Enable Async Scraping"
				)
				return
			browser = await p.chromium.connect_over_cdp(api_key)
		except urllib3.exceptions.NameResolutionError:
			rprint("[red]check your internet connection")
			return

		except playwright._impl._errors.Error as e:  # type: ignore
			if "Account is suspended" in str(e):
				# print(str(e))
				rprint(
					"[red]Bright data account has been suspended by system may your api is exhausted recharge it and try again. You can use `--sync-api` flag after your last command to enable sync scrapping but you may not encounter enought success.  [/red]"
				)
				return
			elif "exists" in str(e):
				# print(str(e))
				rprint(
					"[white] Seems like playwright is not installed. lets aba install it for you... [/white]"
				)
				os.system("playwright install")
			else:
				print(str(e))

		context_browser = await browser.new_context()
		s_one = asyncio.Semaphore(value=10)
		logger.info("Loading pages results ... ")
		async with asyncio.Lock():
			async with asyncio.TaskGroup() as tg:
				with Progress(
					SpinnerColumn(finished_text="[bold green]finished ✓[/bold green]"),
					*Progress.get_default_columns(),
					transient=True,
				) as progress:
					task = progress.add_task("[green blink] async Scraping...", start=False)
					for url in urls_pusher(words=key_words, stop_at=page_results):
						async with asyncio.Lock():
							page = await context_browser.new_page()
						tg.create_task(
							goto_task(
								url=url,
								semaphore=s_one,
								progress=progress,
								task=task,
								tg_instance=tg,
								context_browser=context_browser,
								page=page,
								page_results=page_results,
							)
						)

		write_to_disk(save_in, HTML_PAGE_RESULT)
		run_scrapper_with_success(folder_name=save_in)


def sync_scrapper(*, save_in: str, key_words: str, page_results: int) -> None:
	# pages_urls = _looking_for_urls(keywords=key_words)
	with Progress(
		SpinnerColumn(finished_text="[bold green]finished ✓[/bold green]"),
		*Progress.get_default_columns(),
		transient=True,
	) as progress:
		task = progress.add_task(
			"[green blink] Sync Scraping...",
			start=False,
		)
		playwright = sync_playwright().start()
		try:
			browser = playwright.chromium.launch(headless=True)
		except playwright._impl._errors.Error:  # type: ignore
			rprint(
				"[white] Seems like playwright is not installed. lets aba install it for you... [/white]"
			)
			os.system("playwright install")
		context = browser.new_context()
		for url in urls_pusher(words=key_words, stop_at=page_results):
			page = context.new_page()
			logger.info(f"Loading page {url.split('page=')[1]} ... ")
			try:
				response = page.goto(url, wait_until="domcontentloaded", timeout=0)
				if response is None:
					return None
				logger.info(
					f"Returns the text representation of response body from page {url.split('page=')[1]} ... "
				)
				progress.start_task(task)
				html_content = response.text()
				progress.update(task, advance=100 / page_results)
				global HTML_PAGE_RESULT
				HTML_PAGE_RESULT.append(html_content)
				logger.info(f"Closing the page {url.split('page=')[1]} ... ")
				page.close()
			except PError as e:
				if "ERR_INTERNET_DISCONNECTED" in e.message:
					raise UsageError("Check your internet connection ... ")
	write_to_disk(save_in, HTML_PAGE_RESULT)
	run_scrapper_with_success(folder_name=save_in)


if __name__ == "__main__":
	start_time = time.perf_counter()
	# asyncio.run(async_scrapper(save_in='pc_lenovo', key_words='pc lenovo'),debug=False)
	sync_scrapper(save_in="pc_lenovo", key_words="pc lenovo", page_results=30)
	end_time = time.perf_counter()
	print(f" all those tasks tooks: {end_time - start_time:.2f}")
