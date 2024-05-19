import sys
from typing import Any, Optional

from loguru import logger
from sqlalchemy import Engine
from sqlmodel import Field, Session, SQLModel

# logger.remove(5)
# logger.add(sys.stderr, colorize=True)
class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name : str = Field(index=True)
    alibaba_guranteed: bool
    certifications:str
    minimum_to_order:int
    ordered_or_sold:int
    supplier_id:Optional[int] =  Field(default=None, foreign_key="supplier.id")
    min_price: float
    max_price: float

class Supplier(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name : str = Field(index=True)
    verification_mode : str
    sopi_level  : int
    country_name: str
    years_as_gold_supplier: int

if __name__ == "__main__":...
    # SQLModel.metadata.create_all(engine)