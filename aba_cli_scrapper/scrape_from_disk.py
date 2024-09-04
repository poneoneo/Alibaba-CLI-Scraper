import json
from collections import OrderedDict
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence, Union
from selectolax.parser import Node

import rich
from loguru import logger
from rich.progress import (
	Progress,
	SpinnerColumn,
)
from selectolax.parser import HTMLParser

from aba_cli_scrapper.typed_datas import ProductDict, SupplierDict

from .html_to_disk import json_hunter
from .utils_scrapping import (
	country_name,
	custom_minium_to_oder,
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


@dataclass
class PageParser:
	"""Parse each html page downloaded from alibaba and return a list of suppliers and products.

	:raises TypeError: _description_
	:raises FileNotFoundError: if the targeted folder does not exist
	:return: PageParser object
	:rtype: class `PageParser`
	"""

	# folder path that contains all html files to be scraped
	targeted_folder: Union[str, Path]

	def _retrieve_html_content_as_string(self, html_file: Path):
		"""Retrieve html content from a html file and return it as a string.

		:param html_file: The path of the html file to be read.
		:type html_file: str
		:return: The html content as a string.
		:rtype: str
		"""
		logger.info(f"Retrieving html content from file : {html_file}")
		html_content = html_file.read_text(
			encoding="utf-8",
		)
		logger.info("Html content has been retrieved.")
		return html_content

	@logger.catch(FileNotFoundError)
	def _html_files_explorer(self):
		"""
		Retrieves all the html files in the targeted folder.

		:raises FileNotFoundError: if the targeted folder does not exist
		:return: A list of all html files in the targeted folder
		:rtype: List[Path]
		"""
		targeted_folder = Path(self.targeted_folder).resolve()
		if not targeted_folder.exists():
			raise FileNotFoundError()
		logger.info(f"getting html files from {targeted_folder} ... ")
		html_files = [html_file for html_file in targeted_folder.glob("*.html")]
		logger.info("Html files list has been returned.")
		return html_files

	def _divs_and_dict(self, selector: str = ".fy23-search-card"):
		"""
		Retrieves the div tags that match the given selector and a dictionary of parsed content from the html file
		containing the div tag.

		:param selector: The css selector to retrieve the div tags.
		:type selector: str
		:return: A list of tuples containing the div tag and its corresponding parsed content.
		:rtype: List[Tuple[selectolax.Selector, Dict]]
		"""
		logger.info(f"Retrieving  div tags with class='{selector}' ...")
		divs_and_dict = [
			(
				HTMLParser(self._retrieve_html_content_as_string(html_file)).css(selector),
				json_hunter(
					self._retrieve_html_content_as_string(html_file),
					css_selector="div[id='root']",
				),
			)
			for html_file in self._html_files_explorer()
		]
		logger.info("All expected divs and dict has been retrived ...")

		new_divs_and_dict = []
		for item in divs_and_dict:
			if item[1] is None or item[1] == "":
				continue
			new_divs_and_dict.append((item[0], json.loads(item[1])))  # type: ignore
		return new_divs_and_dict

	def _suppliers_appender(self, offers_list: Sequence[dict], suppliers: list, divs: list[Node]):
		for offer in offers_list:
			suppliers.append({
				"name": offer["companyName"].lower(),
				"verified_type": suppliers_status(tags=divs, offer=offer),
				"sopi_level": offer["displayStarLevel"],
				"country_name": country_name(country_min=offer["countryCode"]),
				"gold_supplier_year": offer["goldSupplierYears"].split(" ")[0],
				"supplier_service_score": float(offer["supplierService"]),
			})
		return suppliers

	def detected_suppliers(self):
		"""Retrieves the detected suppliers from the divs and offers data.
		Returns a list of unique suppliers with their relevant information.
		"""
		suppliers: Sequence[SupplierDict] = list()
		console = rich.console.Console()
		with Progress(
			SpinnerColumn(finished_text="[bold green]finished ✓[/bold green]"),
			*Progress.get_default_columns(),
			console=console,
			transient=True,
		) as progress:
			all_pages_task = progress.add_task(
				description="[blank]Parsing suppliers ...[/blank]",
			)
			# single_page_task = progress.add_task(description="Retrieving suppliers ...", total=1)
			for divs, offers in self._divs_and_dict():
				with open("offers_i.json", "w") as f:
					f.write(json.dumps(offers, indent=4))
				try:
					if offers["offerTotalCount"] == 0:
						continue
				except KeyError:
					if offers["props"]["offerTotalCount"] == 0:
						continue
				try:
					offers_values = offers["offerResultData"]["offers"]
					suppliers_added = self._suppliers_appender(
						offers_list=offers_values, suppliers=suppliers, divs=divs
					)
				except KeyError:
					offers_values = offers["props"]["offerResultData"]["offers"]
					suppliers_added = self._suppliers_appender(
						offers_list=offers_values, suppliers=suppliers, divs=divs
					)
				progress.update(all_pages_task, advance=100 / len(self._divs_and_dict()))
		# removing supliers present twice in supliers dict
		unique_suppliers_tuple = list(OrderedDict((str(d), d) for d in suppliers_added).items())
		unique_suppliers = [supplier_tuple[1] for supplier_tuple in unique_suppliers_tuple]
		return unique_suppliers

	def _produtcs_appender(self, offers_list: Sequence[dict], products: Sequence[ProductDict]):
		for offer in offers_list:
			products.append({
				"name": offer["enPureTitle"].lower(),
				"max_price": get_product_price(all_price_text=offer["price"], which="max"),
				"min_price": get_product_price(all_price_text=offer["price"], which="min"),
				"guaranteed_by_alibaba": is_alibaba_guaranteed(str_status=offer["halfTrust"]),
				"certifications": get_product_certification(offer=offer),
				"minimum_to_order": custom_minium_to_oder(offer["halfTrustMoq"].lower()),
				"ordered_or_sold": ordered_or_sold(offer=offer),
				"supplied_by": offer["companyName"].lower(),
				"product_score": float(offer["productScore"]),
				"review_count": float(offer["reviewCount"]),
				"review_score": float(offer["reviewScore"]),
				"shipping_time_score": float(offer["shippingTime"]),
				"is_full_promotion": is_full_promotion(str_status=offer["isFullPromotion"]),
				"customizable": is_customizable(str_status=offer["customizable"]),
				"instant_order": is_instant_order(str_status=offer["halfTrustInstantOrder"]),
				"trade_product": is_trade_product(str_status=offer["tradeProduct"]),
			})
		return products

	def detected_products(self):
		"""Returns a list of unique products with their relevant information."""
		products: Sequence[ProductDict] = list()
		console = rich.console.Console()
		with Progress(
			SpinnerColumn(finished_text="[bold green]finished ✓[/bold green]"),
			*Progress.get_default_columns(),
			console=console,
			transient=True,
		) as progress:
			all_pages_task = progress.add_task(description="[blank]Parsing products ...[/blank]")
			for divs, offers in self._divs_and_dict():
				try:
					if offers["offerTotalCount"] == 0:
						continue
				except KeyError:
					if offers["props"]["offerTotalCount"] == 0:
						continue
				try:
					offers_values = offers["offerResultData"]["offers"]
					products_added = self._produtcs_appender(
						offers_list=offers_values, products=products
					)
				except KeyError:
					offers_values = offers["props"]["offerResultData"]["offers"]
					products_added = self._produtcs_appender(
						offers_list=offers_values, products=products, divs=divs
					)
				progress.update(all_pages_task, advance=100 / len(self._divs_and_dict()))
		unique_products_tuple = list(OrderedDict((str(d), d) for d in products_added).items())
		# removing supliers present twice in supliers dict
		unique_products = [product_tuple[1] for product_tuple in unique_products_tuple]
		return unique_products
