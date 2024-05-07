
import asyncio
import sys
import time

from loguru import logger
from playwright.async_api import async_playwright
from html_to_disk import write_to_disk

logger.remove(0)
logger.add("pw.log", colorize=True)

SBR_WS_CDP = 'wss://brd-customer-hl_cc4d7c7e-zone-scraping_browser1:p4fgpzg17yly@brd.superproxy.io:9222'

html_content_list = []
# construire la list de liens 
pages_urls = [f"https://french.alibaba.com/trade/search?spm=a2700.galleryofferlist.0.0.538f1619xDyhzJ&fsb=y&IndexArea=product_en&keywords=machines+agricoles&tab=all&&page={page_number}" for page_number in range(1,43)]



async def goto_task(url:str):
    """return the entire html content from each page

    :param url: url of page range 1 to 42 include
    :type url: str
    :return: a string of html content of the current page
    :rtype: str
    """
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp(SBR_WS_CDP)
        context = await browser.new_context()
        page = await context.new_page()
        logger.info(f"getting html content from page {url.split('page=')[1]}")
        await page.goto(url=url,timeout=0)
        html_content = await page.content()
        logger.info(f"html content from page {url.split("page=")[1]} has been returned ")
        await page.close()
        await context.close()
        await browser.close()
        return html_content

async def async_main():
    """Create a list of tasks with `goto` couroutine and pass it to `asyncio.wait` couroutine then wait
    for all the result

    :return: list of html content of each page
    :rtype: list[str]
    """
    start_time = time.perf_counter()
    tasks_list = [ asyncio.create_task(goto_task(url))  for url in pages_urls]
    html_contents = await asyncio.gather(*tasks_list)
    html_content_list.extend([html for html in html_contents if html is not None])
    end_time = time.perf_counter()
    print(f" all those tasks tooks: {end_time-start_time:.2f}")
    return html_content_list


if __name__ == "__main__": 
    asyncio.run(async_main())
    write_to_disk("Alibaba_Scapper_info",html_content_list)



