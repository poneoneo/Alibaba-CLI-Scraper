from typing import Optional

from sqlmodel import Field, SQLModel


class Product(SQLModel, table=True):
	id: Optional[int] = Field(default=None, primary_key=True)
	name: str = Field(index=True, unique=True)
	alibaba_guranteed: bool
	certifications: str
	minimum_to_order: float
	ordered_or_sold: int
	supplier_id: Optional[int] = Field(default=None, foreign_key="supplier.id")
	min_price: float
	max_price: float
	product_score: float
	review_count: float
	review_score: float
	shipping_time_score: float
	is_full_promotion: bool
	is_customizable: bool
	is_instant_order: bool
	trade_product: bool


class Supplier(SQLModel, table=True):
	id: Optional[int] = Field(default=None, primary_key=True)
	name: str = Field(index=True, unique=True)
	verification_mode: str
	sopi_level: int
	country_name: str
	years_as_gold_supplier: int
	supplier_service_score: float


if __name__ == "__main__":
	...
	# SQLModel.metadata.create_all(engine)
