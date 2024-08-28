import json
import pathlib
import unicodedata
from typing import Literal

from loguru import logger
from selectolax.parser import Node


def _remove_dot_from_price(price_as_string: str):
	price = price_as_string.split(".")
	price_dot_removed = ".".join(price[:1])
	return float(price_dot_removed.strip("$US"))


@logger.catch(TypeError)
def get_product_price(all_price_text: str, which: Literal["max", "min"]):
	elt = all_price_text
	if "-" in elt and which == "max":
		max_price = elt.split("-")[1].split("&")[0]
		max_price = unicodedata.normalize("NFKC", max_price)
		max_price = max_price.replace("\u00a0", "").replace(",", ".").replace(" ", "")
		if max_price.count(".") > 1:
			max_price = _remove_dot_from_price(price_as_string=max_price)
			return max_price
		return float(max_price.strip("$US"))

	elif "-" in elt and which == "min":
		min_price = elt.split("-")[0].split("&")[0]
		min_price = unicodedata.normalize("NFKC", min_price)
		min_price = min_price.replace("\u00a0", "").replace(",", ".").replace(" ", "")
		if min_price.count(".") > 1:
			min_price = _remove_dot_from_price(price_as_string=min_price)
			return min_price
		return float(min_price.strip("$US"))
	else:
		strange_price = elt.strip(r"\xa0$US")
		price = unicodedata.normalize("NFKC", strange_price)
		price = price.replace("\u00a0", "").replace(",", ".").replace(" ", "")
		if price.count(".") > 1:
			price = _remove_dot_from_price(price_as_string=price)
			return price
		else:
			return float(price.strip("$US"))


@logger.catch(TypeError)
def is_alibaba_guaranteed(str_status: str):
	if str_status == "false":
		return False
	else:
		return True


@logger.catch(TypeError)
def get_product_certification(offer: dict):
	certifications_name = []
	for info in offer["productCertificates"]:
		certifications_name.append(info["name"])

	return ",".join(certifications_name)


def is_full_promotion(str_status: str):
	if str_status == "false":
		return False
	else:
		return True


def is_customizable(str_status: str):
	if str_status == "false":
		return False
	else:
		return True


def is_instant_order(str_status: str):
	"""Return True if product is instant order, False otherwise.

	:param str_status: String indicating if product is instant order or not.
	:type str_status: str
	:return: True if product is instant order, False otherwise.
	:rtype: bool
	"""
	if str_status == "false":
		return False
	else:
		return True


def is_trade_product(str_status: str):
	"""Return True if product is trade product, False otherwise.

	:param str_status: String indicating if product is trade product or not.
	:type str_status: str
	:return: True if product is trade product, False otherwise.
	:rtype: bool
	"""
	if str_status == "false":
		return False
	else:
		return True


@logger.catch(TypeError)
def suppliers_status(tags: list[Node], offer: dict):
	"""
	Return the verification status of the supplier (unverified, gold, diamond, etc.).

	:param tags: List of Node objects containing the suppliers information.
	:type tags: list[Node]
	:param offer: Dictionary containing the information of the supplier to be searched.
	:type offer: dict
	:return: The verification status of the supplier.
	:rtype: str
	"""
	for tag in tags:
		# print(tag.attributes)
		company_name = tag.css_first("a[data-spm='d_companyName']").text().strip().lower()
		# print(company_name+ "1")
		if company_name == offer["companyName"].lower().strip():
			# print(offer['companyName'].lower().strip()+"2")
			node_a = tag.css_first(".auth-info-group-normal.J_no_jump")
			if node_a is None:
				node_a = tag.css_first(".search-card-e-popper__trigger").child
				# print(node_a.attributes)
				node_a = node_a.css_first(".verified-supplier-icon__wrapper")  # type: ignore
				if node_a is None:
					return "unverified"
				mode = node_a.attributes.get("data-aplus-auto-card-mod")
				return mode.split("=")[2]  # type: ignore
			node_a = node_a.css_first("a.verified-supplier-icon__wrapper")
			if node_a is not None:
				# print(node_a.attributes)
				mode = node_a.attributes.get("data-aplus-auto-card-mod")
				# print(mode)
				mode = mode.split("=")[2]  # type: ignore
				return mode
			return "unverified"
	return "unverified"


@logger.catch(TypeError)
def sopi_level(tag: Node):
	"""
	Return the level of the supplier (from 1 to 5) using the .search-cards-e-star class.

	:param tag: Node object containing the information of the supplier.
	:type tag: Node
	:return: The level of the supplier (from 1 to 5).
	:rtype: int
	"""
	elt = tag.css_first(".search-cards-e-star")
	return len(elt.css(".search-card-e-iconfont"))


@logger.catch(TypeError)
def years_as_supplier_gold(tag: Node):
	"""
	Return the number of years the supplier has been a gold supplier.

	:param tag: Node object containing the information of the supplier.
	:type tag: Node
	:return: The number of years the supplier has been a gold supplier.
	:rtype: int
	"""
	elt = tag.css_first(".search-card-e-supplier__year")
	year = elt.attrs.get("data-aplus-auto-card-mod").split("@@")[1][0]
	return year


def _get_minimum_to_order_tag(tags: list[Node]):
	"""
	Return the tag containing the minimum quantity to order.

	:param tags: List of Node objects containing the information of the supplier.
	:type tags: list[Node]
	:return: The tag containing the minimum quantity to order.
	:rtype: Node
	"""

	for tag in tags:
		element_attr = tag.attrs.get("data-aplus-auto-card-mod")
		# if 'price_negotiated' or "easy_return" not in element_attr:
		#     print(tag.text())
		#     return tag
		if "minimale" in element_attr:
			return tag
		# print(element_attr)


@logger.catch(TypeError)
def minimum_to_order(tag: Node):
	"""
	Return the minimum quantity to order.

	:param tag: Node object containing the information of the product.
	:type tag: Node
	:return: The minimum quantity to order.
	:rtype: int
	"""
	elements = tag.css(".search-card-m-sale-features__item.tow-line")
	if len(elements) != 0:
		element = _get_minimum_to_order_tag(tags=elements)
		if element is None:
			return 0
		number_str = element.text()
		number = number_str.split(":")[1].split()[0].strip()
		return int(number)
	else:
		return 0


def custom_minium_to_oder(scraped_str: str):
	"""
	Return the minimum quantity to order as a float.

	If the scraped string can't be converted to a float, return 0.0.

	:param scraped_str: The scraped string from the page.
	:type scraped_str: str
	:return: The minimum quantity to order.
	:rtype: float
	"""
	try:
		float(scraped_str)
	except ValueError:
		return 0.0
	return float(scraped_str)


@logger.catch(TypeError)
def ordered_or_sold(offer: dict):
	"""
	Return the number of orders or sales of a product.

	:param offer: A dictionary containing the product information.
	:type offer: dict
	:return: The number of orders or sales.
	:rtype: int
	"""
	power_common_info = offer.get("marketingPowerCommon")
	if power_common_info is not None:
		return int(power_common_info["count"])
	else:
		return 0


def _from_abr_to_full_name(country_abr: str):
	"""
	Return the full name of a country from its abbreviation.

	The full name of the country is looked up in the pays_data.json file.

	:param country_abr: The abbreviation of the country (e.g. "FR" for France).
	:type country_abr: str
	:return: The full name of the country in lowercase (e.g. "france" for France).
	:rtype: str
	"""
	p = (pathlib.Path(__file__).parent / "pays_data.json").resolve()
	with open(f"{p}", encoding="utf-8") as f:
		countries = json.load(
			f,
		)
		pays_data = countries["continents_pays"]
		for pays in pays_data:
			# print("two letter code : ", pays["Two_Letter_Country_Code"])
			# print("country abr : ", country_abr)
			if pays["Two_Letter_Country_Code"].lower() == country_abr.lower():
				# print("matched country : ", country_abr)
				return pays["Country_Name"].lower()
			if country_abr.lower() == "uk":
				return "royaume-uni"
		return "unknow"


def country_name(country_min: str):
	"""
	Return the full name of a country from its abbreviation.

	:param country_min: The abbreviation of the country (e.g. "FR" for France).
	:type country_min: str
	:return: The full name of the country in lowercase (e.g. "france" for France).
	:rtype: str
	"""
	return _from_abr_to_full_name(country_abr=country_min)
