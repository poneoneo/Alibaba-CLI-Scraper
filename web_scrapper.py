import asyncio
import sys
import time
from typing import Optional, Union

from loguru import logger
from playwright.async_api import async_playwright,BrowserContext
from decouple import config,Csv
from html_to_disk import write_to_disk
# from scrape_from_disk import suppliers_dictionaries, products_dictionaries, targeted_div_tags, html_files_from_targeted_folder

logger.remove(0)
logger.add(sys.stderr, colorize=True)

SBR_WS_CDP_LIST:list[str]= config("SBR_WS_CDP_LIST", cast=Csv()) # type: ignore

html_content_list = []
# construire la list de liens 
pages_urls = [f"https://french.alibaba.com/trade/search?spm=a2700.galleryofferlist.0.0.538f1619xDyhzJ&fsb=y&IndexArea=product_en&keywords=machines+agricoles&tab=all&&page={page_number}" for page_number in range(1,43)]


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
        logger.info(f"Opening the page {url.split('page=')[1]} ...")
        await page.goto(url, wait_until='domcontentloaded', timeout=0)
        logger.info(f"Getting HTML content from page {url.split('page=')[1]}")
        product_divs = await page.query_selector('.organic-list.viewtype-list', strict=True)
        html_content = await product_divs.inner_html() if product_divs else None
        logger.info(f"HTML content from page {url.split('page=')[1]} has been returned ")
        logger.info(f"Closing the page {url.split('page=')[1]} safely...")
    return html_content


async def async_main() -> None:
    """Create a list of tasks with `goto` coroutine and pass it to `asyncio.wait` coroutine
    then wait for all the results.

    The function takes no arguments and returns None.

    :return: None
    """
    # start the timer to measure the time it takes to run all the tasks
    start_time = time.perf_counter()

    async with async_playwright() as p:
        logger.info("Connecting to CDP and creating the browser...")
        browser = await p.chromium.connect_over_cdp(SBR_WS_CDP_LIST[0],timeout=0)
        context_browser = await browser.new_context()
        logger.info("Creating tasks list...")
        # create the list of tasks to run
        tasks_list = [ asyncio.create_task(goto_task(url, context_browser)) for url in pages_urls ]

        # run all the tasks and gather the results
        logger.info("Running all the tasks ...")
        html_contents = await asyncio.gather(*tasks_list)

        # append all the results to the global list
        html_content_list.extend([html_content for html_content in html_contents if html_content is not None])

    # stop the timer and print the time it took to run all the tasks
    end_time = time.perf_counter()
    print(f" all those tasks tooks: {end_time-start_time:.2f}")

    # write the results to a file
    write_to_disk("Alibaba_Scapper_new", html_content_list)


if __name__ == "__main__": 
    asyncio.run(async_main())