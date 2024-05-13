from web_scrapper import async_main
import asyncio
from loguru import logger

logger.remove(1)
asyncio.run(async_main())