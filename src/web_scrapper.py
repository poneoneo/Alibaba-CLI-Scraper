"""
This script is responsible for scraping data from the Alibaba website.
It uses the Playwright library to navigate through multiple pages
extract HTML content,and save it to disk. The script defines
functions to handle asynchronous tasks,interact with
browser contexts, and gather data from the scraped HTML files.
Additionally, it utilizes loguru for logging purposes and decouple for
managing environment variables.
"""

import asyncio
import time

import playwright
import selectolax
from dotenv import load_dotenv
from html_to_disk import write_to_disk
from info_message import run_scrapper_with_success
from loguru import logger
from playwright.async_api import Page as AsyncPage
from playwright.async_api import async_playwright
from playwright.sync_api import sync_playwright
from rich import print as rprint
from rich.progress import Progress, TaskID, SpinnerColumn, TimeElapsedColumn
from rich.console import Console
import os

load_dotenv()


SBR_WS_CDP_LIST: str = os.environ["SBR_WS_CDP_LIST"]

html_content_list = []

def _browser_parser(html_content: str | bytes, curr_url: str):
    """Parse the HTML content of the page to get the divs with class `.organic-list.viewtype-list`

    :param html_content: The HTML content of the page
    :type html_content: str
    :return: A list of divs with class `.organic-list.viewtype-list`
    :rtype: list
    """
    if html_content is None:
        logger.warning(
            " your page could not be loaded, an empty none value has been returned "
        )
        return None
    body_parser = selectolax.parser.HTMLParser(html_content)
    logger.info(
        f"looking for .organic-list class in the DOM page {curr_url.split('page=')[1]}... "
    )
    product_div = body_parser.css_first(".organic-list")
    if product_div is None:
        return None
    html_result = product_div.html
    if html_result is None:
        logger.warning(
            f"any HTML content from page {curr_url.split('page=')[1]} matched the selector '.organic-list', None value has been returned"
        )
        return None
    else:
        logger.info(
            f"HTML content from page {curr_url.split('page=')[1]} has been returned  "
        )
        return html_result


async def goto_task(
    url: str,
    page: AsyncPage,
    task: TaskID,
    progress: Progress,
    semaphore: asyncio.Semaphore,
) -> str | None:
    """Return the entire HTML content from each page only the divs with class `.organic-list.viewtype-list`

    :param url: URL of page range 1 to 42 include
    :type url: str
    :param context_browser: The browser context to use
    :type context_browser: BrowserContext
    :return: A string of HTML content of the current page, or None if the page has no expected div
    :rtype: Optional[str]
    """
    try:
        async with page:
            logger.info(f"Loading page {url.split('page=')[1]} ... ")
            response = await page.goto(url, wait_until="domcontentloaded", timeout=0)
            if response is None:
                return None
            _lock = asyncio.Lock()
            # async with _lock:
            #     async with semaphore:
            logger.info(f"get response text from web page {url.split('page=')[1]} ... ")
            html_body = await response.text()
            progress.start_task(task)
            progress.update(task, advance=2.385)
            logger.info(f"Closing page {url.split('page=')[1]} ... ")
            await page.close()
            # logger.info(
            #     f"Returns html representation of response body from page {url.split('page=')[1]} ... "
            # )
            return html_body
    except Exception as e:
        logger.error(f"Error processing page {url.split('page=')[1]}: {e}")
        return None


@logger.catch()
def _looking_for_urls(keywords: str) -> list[str]:
    """Return a list of urls for each page of the search results matching the keywords

    :param keyword: Keywords to search
    :type keyword: str
    :return: List of urls
    :rtype: list[str]
    """
    word = keywords.replace(" ", "+").strip()
    pages_urls = [
        f"https://french.alibaba.com/trade/search?spm=a2700.galleryofferlist.0.0.538f1619xDyhzJ&fsb=y&IndexArea=product_en&keywords={word}&tab=all&&page={page_number}"
        for page_number in range(1, 43)
    ]
    return pages_urls


@logger.catch()
async def async_scrapper(*, save_in: str, key_words: str) -> None:
    """Create a list of tasks with `goto` coroutine and pass it to `asyncio.wait` coroutine
    then wait for all the results.
    The function takes no arguments and returns None.
    :return: None
    """
    # start the timer to measure the time it takes to run all the tasks

    # get the list of urls
    pages_urls = _looking_for_urls(keywords=key_words)
    async with async_playwright() as p:
        logger.info("Connecting to CDP and creating the browser... ")
        try:
            browser = await p.chromium.connect_over_cdp(SBR_WS_CDP_LIST)
        except playwright._impl._errors.Error as e:  # type: ignore
            if "Account is suspended" in str(e):
                print(str(e))
                rprint(
                    "[red] Bright data account has been suspended by system. contact me by email: [magenta]onealzero@gmail.com [/magenta] to fix this as soon as possible [/red]"
                )
                return
        context_browser = await browser.new_context()
        tasks_list = []
        logger.info("Creating tasks list... ")
        with Progress(console=Console(record=True),) as progress:
            task = progress.add_task("[green blink] async Scraping...", start=False)
            s_one = asyncio.Semaphore(value=20)
            for idx, url in enumerate(pages_urls, start=0):
                page = await context_browser.new_page()
                print(idx)
                async with s_one:
                    tasks_list.append(
                        asyncio.create_task(
                            goto_task(url=url, page=page, task=task, progress=progress, semaphore=s_one)
                            
                        )
                    )

        logger.info("Running all the tasks ... ")
        html_contents,pending= await asyncio.wait(tasks_list,)
        # html_contents= await asyncio.gather(*tasks_list,)
        if isinstance(html_contents,set):
            html_content_list.extend(
                (html_content,html_content.cancel())[0]
                for html_content in html_contents
                if isinstance(html_content.result(), str)
            )
            
            for i in range(len(pending)):
                print(pending.pop())
        elif isinstance(html_contents,list):
            html_content_list.extend(
                html_content
                for html_content in html_contents
                if isinstance(html_content, str)
            )  
        else:
            pass  
        # await context_browser.close()
        # await browser.close()
        write_to_disk(save_in, html_content_list)
        run_scrapper_with_success(folder_name=save_in)


def sync_scrapper(*, save_in: str, key_words: str):
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    pages_urls = _looking_for_urls(keywords=key_words)
    with Progress(console=Console(record=True), transient=True) as progress:
        task = progress.add_task("[green blink] Sync Scraping...", start=False)
        for idx, url in enumerate(pages_urls, start=0):
            page = context.new_page()
            logger.info(f"Loading page {url.split('page=')[1]} ... ")
            response = page.goto(url, wait_until="domcontentloaded", timeout=0)
            if response is None:
                return None
            logger.info(
                f"Returns the text representation of response body from page {url.split('page=')[1]} ... "
            )
            html_content = response.text()
            progress.start_task(task)
            progress.update(task, advance=2.381)
            parsed_content = _browser_parser(html_content=html_content, curr_url=url)
            html_content_list.append(parsed_content)
            logger.info(f"Closing the page {url.split('page=')[1]} ... ")
            page.close()
    write_to_disk(save_in, html_content_list)
    run_scrapper_with_success(folder_name=save_in)


if __name__ == "__main__":
    start_time = time.perf_counter()
    # asyncio.run(async_scrapper(save_in='pc_lenovo', key_words='pc lenovo'),debug=False)
    sync_scrapper(save_in="pc_lenovo", key_words="pc lenovo")
    end_time = time.perf_counter()
    print(f" all those tasks tooks: {end_time-start_time:.2f}")
    ...
