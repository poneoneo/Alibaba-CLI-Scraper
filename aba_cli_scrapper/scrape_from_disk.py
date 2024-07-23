"""
This Module will gather all datas from html files and build database with two tables, Products and Suppliers

"""

from collections import OrderedDict
from dataclasses import dataclass
import json
from pathlib import Path
from pprint import pprint
from typing import Sequence, Union

import rich
from rich.progress import Progress, TextColumn, BarColumn, TaskProgressColumn, TimeElapsedColumn,SpinnerColumn
from rich.text import Text
from loguru import logger
from selectolax.parser import HTMLParser

from aba_cli_scrapper.typed_datas import ProductDict, SupplierDict
from .utils_scrapping import (
    country_name,
    get_product_certification,
    get_product_price,
    is_alibaba_guaranteed,
    is_customizable,
    is_full_promotion,
    is_instant_order,
    is_trade_product,
    ordered_or_sold,
    suppliers_status,
)
from .html_to_disk import json_parser_to_dict

# logger.remove(4)
# logger.add(sys.stderr,level="DEBUG",colorize=True)


@dataclass
class PageParser:
    """Parse each html page downloaded from alibaba and return a list of suppliers and products

    :raises TypeError: _description_
    :raises FileNotFoundError: if the targeted folder does not exist
    :return: PageParser object
    :rtype: class `PageParser`
    """

    targeted_folder: Union[
        str, Path
    ]  # folder path that contains all html files to be scraped

    def _retrieve_html_content_as_string(self, html_file: Path):
        logger.info(f"Retrieving html content from file : {html_file}")

        if not isinstance(html_file, Path):
            raise TypeError(
                f"html_file must be a Path object but got : {type(html_file)}"
            )

        with open(html_file, "r", encoding="utf-8") as fs:
            html_content = fs.read()
        logger.info("Html content has been retrieved.")
        return html_content
    
    def _retrieve_json_content_as_dict(self, json_file: Path):
        logger.info(f"Retrieving json content from file : {json_file.resolve()}")


        if not isinstance(json_file, Path):
            raise TypeError(
                f"json_file argument must be a Path object but got : {type(json_file)}"
            )

        with open(json_file, "r", encoding="utf-8") as fs:
            json_content_as_dict = json.load(fs,)
        logger.info("Html content has been retrieved.")
        return json_content_as_dict['props']['offerResultData']['offers']

    @logger.catch(FileNotFoundError)
    def _html_files_explorer(self):
        targeted_folder = Path(self.targeted_folder).resolve()
        if not targeted_folder.exists():
            raise FileNotFoundError()
        logger.info(f"getting html files from {targeted_folder} ... ")
        html_files = [html_file for html_file in targeted_folder.glob("*.html")]
        logger.info("Html files list has been returned.")
        return html_files
    
    def _json_files_explorer(self):
        targeted_folder = Path(self.targeted_folder).resolve()
        if not targeted_folder.exists():
            raise FileNotFoundError()
        logger.info(f"getting html files from {targeted_folder} ... ")
        json_files = [html_file for html_file in targeted_folder.glob("*.json")]
        logger.info("json files list has been returned.")
        return json_files

    def _divs_and_dict(self, selector: str = ".fy23-search-card"):
        """
        Retrieve div tags with a specified selector class from HTML files, parse them, and return a list of tuples containing the parsed div tags and corresponding JSON data as dictionaries.
        
        :param selector: The CSS selector for the div tags to retrieve. Defaults to ".fy23-search-card".
        :return: A list of tuples where each tuple contains the parsed div tags and the corresponding JSON data as dictionaries.
        :rtype: List[Tuple[Node, Dict]]
        """
        logger.info(f"Retrieving  div tags with class='{selector}' ...")
        divs_and_dict = [
            (
            HTMLParser(self._retrieve_html_content_as_string(html_file)).css(selector),
            json_parser_to_dict(self._retrieve_html_content_as_string(html_file), css_selector="body > div.container > script[type='text/javascript'] + script"),
                )
            for html_file in self._html_files_explorer() 
        ]
        logger.info("All expected divs and dict has been retrived ...")
        # TODO: add good items directly in a new list instead of removing them
        _ = [divs_and_dict.pop(divs_and_dict.index(item)) for item in divs_and_dict if item[0] is not None and item[1] is None] # remove none tuple from list
        new_divs_and_dict = []
        for item in divs_and_dict:
            # print("hello")
            # print(item[1])
            # print(type(item[1]))
            new_divs_and_dict.append((item[0],json.loads(item[1]))) # type: ignore

        return new_divs_and_dict


    def _offers_builder(self,):
        offers_dict: list[dict[str, str]] = [self._retrieve_json_content_as_dict(json_file) for json_file in self._json_files_explorer()]
        return offers_dict
    def detected_suppliers(self):
        """
        Retrieves the detected suppliers from the divs and offers data.
        Returns a list of unique suppliers with their relevant information.
        """

        suppliers: Sequence[SupplierDict] = list()
        console = rich.console.Console()
        with Progress(SpinnerColumn(finished_text="[bold green]finished ✓[/bold green]"), *Progress.get_default_columns(),console=console,transient=True) as progress:
            all_pages_task = progress.add_task(description="[blank]Parsing suppliers ...[/blank]")
            # single_page_task = progress.add_task(description="Retrieving suppliers ...", total=1)
            for divs, offers in self._divs_and_dict():
                    if offers['props']['offerResultData']['totalCount'] == 0:
                        continue 
                    for offer in offers['props']['offerResultData']['offers']: 
                        suppliers.append(
                                {
                                "name": offer['companyName'].lower(),   
                                "verified_type": suppliers_status(tags=divs, offer=offer),
                                "sopi_level": offer['displayStarLevel'],
                                "country_name": country_name(country_min=offer['countryCode']), 
                                "gold_supplier_year": offer['goldSupplierYears'].split(" ")[0], 
                                "supplier_service_score": float(offer["supplierService"])  
                            }
    
                        )
                    progress.update(all_pages_task, advance=100/len(self._divs_and_dict()))
        # removing supliers present twice in supliers dict
        unique_suppliers_tuple = list(
            OrderedDict((str(d), d) for d in suppliers).items()
        )
        # print(unique_suppliers_tuple)
        unique_suppliers = [
            supplier_tuple[1] for supplier_tuple in unique_suppliers_tuple
        ]
        return unique_suppliers

    def detected_products(self):
        """
        Returns a list of unique products with their relevant information.
        """
        products: Sequence[ProductDict] = list()
        console = rich.console.Console()
        with Progress(SpinnerColumn(finished_text="[bold green]finished ✓[/bold green]"),*Progress.get_default_columns(),console=console,transient=True) as progress:
            all_pages_task = progress.add_task(description="[blank]Parsing products ...[/blank]") 
            for divs, offers in self._divs_and_dict():
                if offers['props']['offerResultData']['totalCount'] == 0:
                    continue 
                # print(f"total count : {offers['props']['offerResultData']['totalCount']}")
                for offer in offers['props']['offerResultData']['offers']: 
                    products.append(
                            {
                                "name": offer['enPureTitle'].lower(),
                                "max_price": get_product_price(all_price_text=offer['price'], which="max"),
                                "min_price": get_product_price(all_price_text=offer['price'], which="min"),
                                "guaranteed_by_alibaba": is_alibaba_guaranteed(str_status=offer['halfTrust']),
                                "certifications": get_product_certification(offer=offer),
                                "minimum_to_order": int(offer['halfTrustMoq'].lower()),
                                "ordered_or_sold": ordered_or_sold(offer=offer),
                                "supplied_by": offer['companyName'].lower(),
                                "product_score": float(offer["productScore"]),
                                "review_count": float(offer["reviewCount"]),
                                "review_score": float(offer["reviewScore"]),
                                "shipping_time_score":float(offer["shippingTime"]),
                                "is_full_promotion": is_full_promotion(str_status=offer["isFullPromotion"]),
                                "customizable" : is_customizable(str_status=offer["customizable"]),
                                "instant_order": is_instant_order(str_status=offer["halfTrustInstantOrder"]),
                                "trade_product": is_trade_product(str_status=offer['tradeProduct'])
                                
                            }
                        )
                progress.update(all_pages_task, advance=100/len(self._divs_and_dict()))
        unique_products_tuple = list(
            OrderedDict((str(d), d) for d in products).items()) 
        # removing supliers present twice in supliers dict
        unique_products = [product_tuple[1] for product_tuple in unique_products_tuple]
        return unique_products


if __name__ == "__main__":
    pp = PageParser(targeted_folder="Alibaba_Scapper_new")
    dt = pp.detected_suppliers()
    for d in dt:
        pprint(d)
    # help(pp)
