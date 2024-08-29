from typing import TypedDict


class ProductDict(TypedDict):
	name: str
	guaranteed_by_alibaba: bool
	certifications: str
	minimum_to_order: float
	ordered_or_sold: int
	min_price: float
	max_price: float
	product_score: float
	review_count: float
	review_score: float
	shipping_time_score: float
	is_full_promotion: bool
	customizable: bool
	instant_order: bool
	trade_product: bool
	supplied_by: str


class SupplierDict(TypedDict):
	name: str
	verified_type: str
	sopi_level: int
	country_name: str
	gold_supplier_year: int
	supplier_service_score: float
