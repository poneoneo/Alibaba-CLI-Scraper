
import asyncio
import html
from lib2to3.fixes.fix_input import context
import sys
from pprint import pprint
import typing

from loguru import logger
from playwright.async_api import async_playwright,Browser, BrowserContext
from playwright.sync_api import sync_playwright
from selectolax.parser import HTMLParser

logger.remove(0)
logger.add(sys.stderr, colorize=True)




# construire la list de liens 
pages_urls = [f"https://french.alibaba.com/trade/search?spm=a2700.galleryofferlist.0.0.538f1619xDyhzJ&fsb=y&IndexArea=product_en&keywords=machines+agricoles&tab=all&&page={page_number}" for page_number in range(1,43)]


def get_content_page(context_browser:BrowserContext,url):
        logger.info("Ouverture d'une nouvelle page")
        page = context_browser.new_page()
        logger.info(f"go to page {url}")
        page.goto(url)
        logger.info(f"html content from page {url.split("page=")[1]} has been returned ")
        html_content = page.content()
        page.close()
        return html_content

async def async_get_content_page(url:str):
    async with async_playwright() as p:
        logger.info("Ouverture du navigateur")
        browser = await p.chromium.launch()
        logger.info("Ouverture d'un Onglet")
        page = await browser.new_page()
        logger.info("aller sur alibaba.com")
        await page.goto(pages_urls[0])
        logger.info("Recuperation du contenu html de la page")
        html_content = await page.content()
        return html_content
    
async def goto_task(context_browser:BrowserContext, url:str):
    page = await context_browser.new_page()
    logger.info(f"getting html content from page {url.split('page=')[1]}")
    await page.goto(f"{url}")
    html_content = await page.content()
    logger.info(f"html content from page {url.split("page=")[1]} has been returned ")
    await page.close()
    return html_content

async def async_main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context_browser: BrowserContext = await browser.new_context()
        async with asyncio.TaskGroup() as tg:
            for url in pages_urls:
                tg.create_task(goto_task(context_browser=context_browser, url=url))

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context_browser = browser.new_context()
        for url in pages_urls:
            get_content_page(context_browser=context_browser,url=url)

if __name__ == "__main__":
    asyncio.run(async_main())
    
