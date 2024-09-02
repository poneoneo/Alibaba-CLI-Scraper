"""This script is responsible for scraping data from the Alibaba website.
It uses the Playwright library to navigate through multiple pages
extract HTML content,and save it to disk. The script defines
functions to handle asynchronous tasks,interact with
browser contexts, and gather data from the scraped HTML files.
Additionally, it utilizes loguru for logging purposes and decouple for
managing environment variables.
"""

import asyncio
from asyncio import TaskGroup
from typing import Optional

from loguru import logger
from playwright.async_api import BrowserContext
from playwright.async_api import Page as AsyncPage
from rich.progress import Progress, TaskID


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


if __name__ == "__main__":
	pass
