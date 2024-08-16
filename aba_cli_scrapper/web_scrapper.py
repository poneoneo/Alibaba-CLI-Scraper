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
import os
import time
from asyncio import TaskGroup
from typing import Optional

import playwright
import playwright.sync_api
import selectolax
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
from tenacity import retry, stop_after_attempt

from . import SBR_WS_CDP_LIST
from .html_to_disk import write_to_disk
from .info_message import run_scrapper_with_success

# SECRETS_KEYS = dotenv_values(".env")
HTML_PAGE_RESULT = []


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


@retry(stop=stop_after_attempt(3))
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
    """Return the entire HTML content from each page only the divs with class `.organic-list.viewtype-list`

    :param url: URL of page range 1 to 42 include
    :type url: str
    :param context_browser: The browser context to use
    :type context_browser: BrowserContext
    :return: A string of HTML content of the current page, or None if the page has no expected div
    :rtype: Optional[str]
    """
    # page = await context_browser.new_page()
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
        yield f"https://french.alibaba.com/trade/search?spm=a2700.galleryofferlist.0.0.538f1619xDyhzJ&fsb=y&IndexArea=product_en&keywords={words}&tab=all&&page={i}"


@logger.catch()
async def async_scrapper(*, save_in: str, key_words: str, page_results: int) -> None:
    """Create a list of tasks with `goto` coroutine and pass it to `asyncio.wait` coroutine
    then wait for all the results.
    The function takes no arguments and returns None.
    :return: None
    """
    async with async_playwright() as p:
        logger.info("Connecting to CDP and creating the browser... ")
        try:
            # response = requests.get("http://geo.brdtest.com/mygeo.json")
            # print(response.raise_for_status())
            # country_name = response.json()["country"]
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
                    task = progress.add_task(
                        "[green blink] async Scraping...", start=False
                    )
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
    print(f" all those tasks tooks: {end_time-start_time:.2f}")
