"""
This script is responsible for scraping data from the Alibaba website. It uses the Playwright library to navigate through multiple pages, extract HTML content, and save it to disk. The script defines functions to handle asynchronous tasks, interact with browser contexts, and gather data from the scraped HTML files. Additionally, it utilizes loguru for logging purposes and decouple for managing environment variables.
"""

import asyncio
import time
from typing import Optional

from loguru import logger
from playwright.async_api import async_playwright,BrowserContext
from decouple import config,Csv
from html_to_disk import write_to_disk



SBR_WS_CDP_LIST:list[str]= config("SBR_WS_CDP_LIST", cast=Csv()) # type: ignore

html_content_list = []



async def goto_task(
    url: str,
    context_browser: BrowserContext,
) -> Optional[str]:
    """Return the entire HTML content from each page only the divs with class `.organic-list.viewtype-list`

    :param url: URL of page range 1 to 42 include
    :type url: str
    :param context_browser: The browser context to use
    :type context_browser: BrowserContext
    :return: A string of HTML content of the current page, or None if the page has no expected div
    :rtype: Optional[str]
    """
    page = await context_browser.new_page()  
    async with page:
        logger.info(f"Loading page {url.split('page=')[1]} ...")
        logger.info("Waiting for 3 milliseconds ...")
        await page.wait_for_timeout(300)
        await page.goto(url, timeout=0,wait_until='domcontentloaded')
        logger.info(f"Waiting for .organic-list class to be attached in the DOM page {url.split('page=')[1]}...")
        await page.wait_for_selector('.organic-list',state='visible')
        element_handler = await page.query_selector('.organic-list')
        # await product_divs.inner_html()
        # product_divs_locator = page.locator('.organic-list').all()
        # logger.info(f"Getting elements content with `.organic-list` class  from page {url.split('page=')[1]}")

        html_content = None if element_handler is None else await element_handler.inner_html()
        print(html_content)
        if html_content is None:
            logger.warning(f"any HTML content from page {url.split('page=')[1]} matched the selector '.organic-list', None has been returned")
            return html_content
    logger.info(f"HTML content from page {url.split('page=')[1]} has been returned ")
    # logger.info(f"Closing page {url.split('page=')[1]} and return HTML content ...")
    # await page.close()
    return html_content


@logger.catch()
def _looking_for_urls(keywords:str) -> list[str]:
    """Return a list of urls for each page of the search results matching the keywords

    :param keyword: Keywords to search
    :type keyword: str
    :return: List of urls
    :rtype: list[str]
    """
    word = keywords.replace(" ","+").strip()
    pages_urls = [f"https://french.alibaba.com/trade/search?spm=a2700.galleryofferlist.0.0.538f1619xDyhzJ&fsb=y&IndexArea=product_en&keywords={word}&tab=all&&page={page_number}" for page_number in range(1,43)]
    return pages_urls



@logger.catch()
async def async_scrapper(save_in:str,key_words:str) -> None:
    """Create a list of tasks with `goto` coroutine and pass it to `asyncio.wait` coroutine
    then wait for all the results.
    The function takes no arguments and returns None.
    :return: None
    """
    # start the timer to measure the time it takes to run all the tasks
    start_time = time.perf_counter()

    # get the list of urls
    pages_urls = _looking_for_urls(keywords=key_words)

    async with async_playwright() as p:
        logger.info("Connecting to CDP and creating the browser...")
        browser = await p.chromium.connect_over_cdp(SBR_WS_CDP_LIST[0])
        context_browser = await browser.new_context()
        logger.info("Creating tasks list...")
        async with asyncio.TaskGroup() as tg:
            tasks = [tg.create_task(goto_task(url, context_browser)) for url in pages_urls]
            logger.info("Running all the tasks ...")
            html_contents = [await task for task in tasks if task is not None]
            
        # logger.info("Closing the context of the browser ...")
        # await context_browser.close()
        logger.info("Closing the browser ...")
        await browser.close()

        # create the list of tasks to run
        # logger.info("Creating tasks list...")
        # tasks_list = [ asyncio.create_task(goto_task(url, context_browser)) for url in pages_urls ]

        # run all the tasks and gather the results
        # logger.info("Running all the tasks ...")
        # html_contents = await asyncio.gather(*tasks_list)

        # append all the results to the global list
        html_content_list.extend([html_content for html_content in html_contents if html_content is not None])

    # stop the timer and print the time it took to run all the tasks
    end_time = time.perf_counter()
    print(f" all those tasks tooks: {end_time-start_time:.2f}")
    # write the results to a file
    write_to_disk(save_in, html_content_list)


if __name__ == "__main__": ...
    # asyncio.run(async_scrapper('Velo_vtt'))