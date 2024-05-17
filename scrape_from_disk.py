"""
This Module will gather all datas from html files and build database with two tables, Products and Suppliers 

"""
from pprint import pprint
import sys
from collections import OrderedDict
from pathlib import Path

from dataclasses import dataclass
from typing import Union
from loguru import logger
from selectolax.parser import HTMLParser, Node

from utils_scrapping import (
    country_name,
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

@dataclass
class PageParser:
    targeted_folder:Union[str,Path] #folder path that contains all html files to be scraped

    def _retrieve_html_content_as_string(self,html_file:Path):
        logger.info(f"Retrieving html content from file : {html_file}")

        if not isinstance(html_file,Path):
            raise TypeError(f"html_file must be a Path object but got : {type(html_file)}")
        
        with open(html_file,"r",encoding='utf-8') as fs:
            html_content = fs.read()
        logger.info("Html content has been retrieved.")
        return html_content
    
    def _html_files_explorer(self):
        targeted_folder = Path(self.targeted_folder)
        if not targeted_folder.exists():
            raise FileNotFoundError()
        logger.info(f"getting html files from {targeted_folder} ... ")
        html_files = [html_file for html_file in targeted_folder.glob("*.html")]
        logger.info("Html files list has been returned.")
        return html_files
    
    def _looking_for_divs(self,selector:str ='.fy23-search-card'):
        logger.info(f"Retrieving  div tags with class='{selector}' ...")
        html_contents = [ self._retrieve_html_content_as_string(html_file) for html_file in self._html_files_explorer()]
        selected_div_tags = [HTMLParser(html_content).css(selector) for html_content in html_contents]
        logger.info("All expected div has been retrived ...")
        return selected_div_tags
    
    def detected_suppliers(self):
        suppliers :list[dict[str,Node|str|int|None]] = list()
        selected_div_tags_from_all_pages = self._looking_for_divs()
        for page_number,page_divs in enumerate(selected_div_tags_from_all_pages,start=1):
            logger.info(f"Building suppliers dictionary for all suppliers in page {page_number} ...")
            for div in page_divs:
                suppliers.append(
                    {
                        'name':div.css_first(".search-card-e-company").text().lower(),
                        'verified_type':suppliers_status(tag=div),
                        'sopi_level': sopi_level(tag=div),
                        'country_name':country_name(tag=div),
                        'gold_supplier_year': years_as_supplier_gold(tag=div)
                    }
                )
        #removing supliers present twice in supliers dict
        unique_suppliers_tuple = list(OrderedDict((str(d),d) for d in suppliers).items())
        unique_suppliers = [supplier_tuple[1] for supplier_tuple in unique_suppliers_tuple]
        return unique_suppliers
    
    def detected_products(self):
        products :list[dict[str,Node|str|int|None|float]] = []
        selected_div_tags_from_all_pages = self._looking_for_divs()
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
        unique_products = [product_tuple[1] for product_tuple in unique_products_tuple] 
        return unique_products
    



if __name__ == "__main__":
    pp = PageParser(targeted_folder="Alibaba_Scapper_new")
    dt = pp.detected_suppliers()
    for d in dt:
        pprint(d)
    # help(pp)