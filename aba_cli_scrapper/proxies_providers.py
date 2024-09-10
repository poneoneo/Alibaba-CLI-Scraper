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

import urllib3
from click import UsageError
from loguru import logger
from playwright.async_api import async_playwright, APIRequestContext
from playwright.sync_api import Error as PError
from playwright.sync_api import sync_playwright
from rich import print as rprint
from rich.progress import Progress, SpinnerColumn, TaskID
import typer

from . import BRIGHT_DATA_API_KEY, SYPHOON_API_KEY
from .html_to_disk import write_to_disk
from .info_message import run_scrapper_with_success
from .proxies_utils import urls_pusher, goto_task, HTML_PAGE_RESULT


class BrightDataProxyProvider:
	BD_API_KEY = BRIGHT_DATA_API_KEY

	@classmethod
	@logger.catch()
	async def async_scraper(cls, *, save_in: str, key_words: str, page_results: int) -> None:
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
		if cls.BD_API_KEY == "":
			rprint("[red]You need to set your  API key to use BrightData proxies ... [/red]")
			return typer.Exit(code=1)
		with Progress(
			SpinnerColumn(finished_text="[bold green]finished ✓[/bold green]"),
			*Progress.get_default_columns(),
			transient=True,
		) as progress:
			async with async_playwright() as p:
				logger.info("Connecting to CDP and creating the browser... ")
				try:
					# print("rt")
					if cls.BD_API_KEY == "":
						rprint(
							"[red]You need to set your SCRAPING BROWSER API key from BrightData to Enable Async Scraping"
						)
						return
					browser = await p.chromium.connect_over_cdp(cls.BD_API_KEY)
				except urllib3.exceptions.NameResolutionError:
					rprint("[red]check your internet connection")
					return
				except Exception as e:
					if "Account is suspended" in str(e):
						rprint(
							"[red]Bright data account has been suspended by system may your api is exhausted recharge it and try again. You can use `--sync-api` flag after your last command to enable sync scrapping but you may not encounter enought success.  [/red]"
						)
						return
					elif "exists" in str(e):
						rprint(
							"[white] Seems like playwright is not installed or needs to be update. lets aba install it for you... [/white]"
						)
						os.system("playwright install")
						return typer.Exit(code=1)
					elif "WebSocket error" in str(e):
						rprint(
							"[red]Web Socket is disconnected. You May need to activate your Internet connexion"
						)
						return typer.Exit(code=1)
					elif "try connecting via ws" in e.message:
						rprint(
							"[red] You must to set a SCRAPING BROWSER API key (e.g 'ws://127.0.0.1:3000') to enable connection via websocket. "
						)
						return typer.Exit(code=1)
					else:
						rprint(f"[red]Unexpected error occured : \n{e}")
						return typer.Exit(code=1)

				context_browser = await browser.new_context()
				s_one = asyncio.Semaphore(value=10)
				logger.info("Loading pages results ... ")
				async with asyncio.Lock():
					async with asyncio.TaskGroup() as tg:
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

	@classmethod
	def sync_scraper(cls, *, save_in: str, key_words: str, page_results: int) -> None:
		if cls.BD_API_KEY == "":
			rprint("[red]You need to set your  API key to use BrightData proxies ... [/red]")
			return typer.Exit(code=1)
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
				browser = playwright.chromium.connect_over_cdp(cls.BD_API_KEY)
			except PError as e:
				if "exists" in e.message:
					rprint(
						"[white] Seems like playwright is not installed or need to be update. lets aba install it for you... [/white]"
					)
					os.system("playwright install")
					return typer.Exit(code=1)
				elif "try connecting via ws" in e.message:
					rprint(
						"[red] You must to set a SCRAPING BROWSER API key (e.g 'ws://127.0.0.1:3000') to enable connection via websocket. "
					)
					return typer.Exit(code=1)
				else:
					rprint(f"[red]Unexpected error occured : \n{e}")
					return typer.Exit(code=1)
			context = browser.new_context()
			for url in urls_pusher(words=key_words, stop_at=page_results):
				logger.info(f"Loading page {url.split('page=')[1]} ... ")
				page = context.new_page()
				try:
					response = page.goto(url, wait_until="domcontentloaded", timeout=0)
					if response is None:
						return None
					logger.info(
						f"Returns the text representation of response body from page {url.split('page=')[1]} ... "
					)
					html_content = response.text()
					progress.start_task(task)
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


class SyphoonProxyProvider:
	SP_API_KEY = SYPHOON_API_KEY

	@classmethod
	@logger.catch()
	async def custom_goto_task(
		cls,
		url: str,
		api_context: APIRequestContext,
		task: TaskID,
		progress: Progress,
		semaphore: asyncio.Semaphore,
		tg_instance: asyncio.TaskGroup,
		page_results: int,
	):
		logger.info(f"fetching page {url.split('page=')[1]} ... ")
		response = await api_context.post(
			"http://api.syphoon.com/",
			data={
				"key": cls.SP_API_KEY,
				"method": "get",
				"url": url,
			},
			timeout=0,
		)
		if response is None:
			return None
		logger.info(f"get response from syphoon api for: {url.split('page=')[1]} ... ")
		progress.start_task(task)
		html_body = await response.text()
		progress.update(task, advance=100 / page_results)
		global HTML_PAGE_RESULT
		HTML_PAGE_RESULT.append(html_body)
		logger.info(f"Closing page {url.split('page=')[1]} ... ")
		return

	@classmethod
	@logger.catch()
	def sync_scraper(cls, *, save_in: str, key_words: str, page_results: int) -> None:
		if cls.SP_API_KEY == "":
			rprint("[red]You need to set your  API key to use Syphoon proxies ... [/red]")
			return typer.Exit(code=1)
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
			except PError:
				rprint(
					"[white] Seems like playwright is not installed or needs to be update. lets aba install it for you... [/white]"
				)
				os.system("playwright install")
				return typer.Exit(code=1)
			context = browser.new_context()
			api_request = context.request
			for url in urls_pusher(words=key_words, stop_at=page_results):
				logger.info(f"Loading page {url.split('page=')[1]} ... ")
				try:
					response = api_request.post(
						"http://api.syphoon.com/",
						data={
							"key": cls.SP_API_KEY,
							"method": "get",
							"url": url,
						},
						timeout=0,
					)
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
				except PError as e:
					if "ERR_INTERNET_DISCONNECTED" in e.message:
						raise UsageError("Check your internet connection ... ")
		write_to_disk(save_in, HTML_PAGE_RESULT)
		run_scrapper_with_success(folder_name=save_in)

	@classmethod
	@logger.catch()
	async def async_scraper(cls, *, save_in: str, key_words: str, page_results: int) -> None:
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
		browser = None
		if cls.SP_API_KEY == "":
			rprint("[red]You need to set your  API key to use Syphoon proxies ... [/red]")
			return typer.Exit(code=1)
		with Progress(
			SpinnerColumn(finished_text="[bold green]finished ✓[/bold green]"),
			*Progress.get_default_columns(),
			transient=True,
		) as progress:
			async with async_playwright() as p:
				logger.info("Connecting to CDP and creating the browser... ")
				try:
					# print("rt")

					if cls.SP_API_KEY == "":
						rprint(
							"[red]You need to set your SCRAPING BROWSER API key from BrightData or proxies API key from Syphoon"
						)
						return
					browser = await p.chromium.launch()
				except PError as e:  # type: ignore
					if "Account is suspended" in str(e):
						# print(str(e))
						rprint(
							"[red]Bright data account has been suspended by system may your api is exhausted recharge it and try again. You can use `--sync-api` flag after your last command to enable sync scrapping but you may not encounter enought success.  [/red]"
						)
						return typer.Exit(code=1)
					elif "exists" in str(e):
						# print(str(e))
						rprint(
							"[white] Seems like playwright is not installed or needs to be update. lets aba install it for you... [/white]"
						)
						os.system("playwright install")
						return typer.Exit(code=1)
					elif "WebSocket error" in str(e):
						rprint(
							"[red]Web Socket is disconnected. You May need to activate your Internet connexion"
						)
						return typer.Exit(code=1)
					else:
						rprint("[red]Unexpected error occured ...")
						return typer.Exit(code=1)
				context_browser = await browser.new_context(base_url="http://api.syphoon.com/")
				s_one = asyncio.Semaphore(value=2)
				logger.info("Loading pages results ... ")
				api_request_context = context_browser.request
				async with asyncio.Lock():
					async with asyncio.TaskGroup() as tg:
						task = progress.add_task("[green blink] async Scraping...", start=False)
						for url in urls_pusher(words=key_words, stop_at=page_results):
							async with asyncio.Lock():
								tg.create_task(
									cls.custom_goto_task(
										url=url,
										api_context=api_request_context,
										task=task,
										progress=progress,
										semaphore=s_one,
										tg_instance=tg,
										page_results=page_results,
									)
								)
				write_to_disk(save_in, HTML_PAGE_RESULT)
				run_scrapper_with_success(folder_name=save_in)
