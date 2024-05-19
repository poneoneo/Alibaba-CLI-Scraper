import sys
from web_scrapper import async_scrapper
import asyncio
from loguru import logger
from scrape_from_disk import PageParser
from engine_and_database import add_products_to_db, create_sqlite_db,save_all_changes,add_suppliers_to_db
from sqlmodel import SQLModel

logger.remove(0)
logger.add(sys.stderr, colorize=True)
def app(key_words:str,save_in:str,database_name:str) -> None:
    asyncio.run(async_scrapper(save_in=save_in,key_words=key_words))
    page_parser = PageParser(targeted_folder=save_in)
    suppliers = page_parser.detected_suppliers()
    products = page_parser.detected_products()
    sqlite_engine = create_sqlite_db(db_name=database_name)
    save_all_changes(engine_db=sqlite_engine,sql_model=SQLModel)
    add_suppliers_to_db(suppliers=suppliers,engine_db=sqlite_engine)
    add_products_to_db(products=products,engine_db=sqlite_engine)
    save_all_changes(engine_db=sqlite_engine,sql_model=SQLModel)

if __name__ == "__main__":
    # app(key_words=sys.argv[1],save_in=sys.argv[2],database_name=sys.argv[3])
    app(key_words="samsung galaxy s20 plus",save_in="samsung",database_name="samsung")