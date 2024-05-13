"""
This Module will gather all datas necessary to build database with two tables, Products and Suppliers 

"""
from pprint import pprint
import sys
from collections import OrderedDict
from pathlib import Path

from loguru import logger
from selectolax.parser import HTMLParser, Node

from utils_scrapping import (
    get_product_certification,
    get_product_price,
    is_alibaba_guaranteed,
    sopi_level,
    suppliers_status,
    years_as_supplier_gold,
    minimum_to_order,
    ordered_or_sold
)

logger.remove(0)
logger.add(sys.stderr,level="DEBUG",colorize=True)

def _retrieve_html_content(html_file:Path):
    logger.info(f"Retrieving html content from file : {html_file}")
    with open(html_file,"r",encoding='utf-8') as fs:
        html_content = fs.read()
    logger.info("Html content has been retrieved.")
    return html_content

@logger.catch(FileNotFoundError)
def html_files_from_targeted_folder(targeted_directory:str):
    targeted_folder = Path(targeted_directory)
    if not targeted_folder.exists():
        raise FileNotFoundError()
    logger.info(f"getting html files from {targeted_folder} ... ")
    html_files = [html_file for html_file in targeted_folder.glob("*.html")]
    logger.info("Html files list has been returned.")
    return html_files

@logger.catch(TypeError)
def targeted_div_tags(html_files:list[Path]):
    logger.info("Retrieving  div tags with class='.fy23-search-card' ...")
    html_contents = [ _retrieve_html_content(html_file) for html_file in html_files]
    selected_div_tags = [HTMLParser(html_content).css(".fy23-search-card") for html_content in html_contents]
    logger.info("All expected div has been retrived ...")
    return selected_div_tags

# build a list of supliers dictionaries
def suppliers_dictionaries(selected_div_tags_from_all_pages:list[list[Node]]):
    suppliers :list[dict[str,Node|str|int|None]] = []
    for page_number,page_divs in enumerate(selected_div_tags_from_all_pages,start=1):
        logger.info(f"Building suppliers dictionary for all suppliers in page {page_number} ...")
        for div in page_divs:
            suppliers.append(
                {
                    'name':div.css_first(".search-card-e-company").text().lower(),
                    'verified_type':suppliers_status(tag=div),
                    'sopi_level': sopi_level(tag=div),
                    'country_abr':div.css_first('.search-card-e-country-flag__wrapper').css_first('img').attrs.get('alt'),
                    'gold_supplier_year': years_as_supplier_gold(tag=div)
                }
            )
    unique_suppliers_tuple = list(OrderedDict((str(d),d) for d in suppliers).items())#removing supliers present twice in supliers dict
    unique_suppliers = [supplier_tuple[1] for supplier_tuple in unique_suppliers_tuple]
    return unique_suppliers

def products_dictionaries(selected_div_tags_from_all_pages:list[list[Node]]):
    products :list[dict[str,Node|str|int|None|float]] = []
    for page_number,page_divs in enumerate(selected_div_tags_from_all_pages,start=1):
        logger.info(f"Building products dictionary for all products in page {page_number} ...")
        for div in page_divs:
            products.append(
                {
                    'name':div.css_first(".search-card-e-title").text().lower(),
                    'max_price':get_product_price(tag=div,which='max'),
                    'min_price':get_product_price(tag=div,which='min'),
                    'guaranteed_by_alibaba': is_alibaba_guaranteed(tag=div),
                    'certifications': get_product_certification(tag=div),
                    'minimum_to_order':minimum_to_order(tag=div),
                    'ordered_or_sold':ordered_or_sold(tag=div),
                    "supplied_by":div.css_first(".search-card-e-company").text().lower()
                }
            )
    unique_products_tuple = list(OrderedDict((str(d),d) for d in products).items())#removing supliers present twice in supliers dict
    unique_products = [supplier_tuple[1] for supplier_tuple in unique_products_tuple ]
    return unique_products




if __name__ == "__main__":
    html_files = html_files_from_targeted_folder(targeted_directory="Alibaba_Pages_results")
    div_tags = targeted_div_tags(html_files=html_files[:2])
    # suppliers = suppliers_dictionaries(div_tags)
    # pprint(suppliers)
    # pprint(len(suppliers))

    products = products_dictionaries(div_tags)
    pprint(products)
    pprint(len(products))