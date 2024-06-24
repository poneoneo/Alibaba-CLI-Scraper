from pprint import pprint
from typing import Any

from loguru import logger
from models import Product, Supplier  # noqa: F401
from MySQLdb import OperationalError
from sqlalchemy.engine import Engine
from sqlmodel import Session, SQLModel, create_engine, select  # noqa: F401


def create_db_engine(db_name: str = "", db_url: str = ""):
    if db_url == "":
        engine = create_engine(f"sqlite:///{db_name}.sqlite")
    if db_url != "":
        engine = create_engine(db_url)
    return engine


# engine = create_engine("sqlite:///iphones_xs.sqlite")
def save_all_changes(
    engine_db: Engine,
    sql_model,
):
    """
    A function that saves all changes by creating all metadata for a given SQL model on the specified engine database.

    Parameters:
    engine_db (Engine): The database engine to use for saving changes.
    sql_model: The SQL model for which to create the metadata.
    """
    logger.info("Saving all changes ...")
    try:
        sql_model.metadata.create_all(engine_db)
    except OperationalError as e:
        logger.error(f"Errors has occured: {e}")
        raise OperationalError from e


def add_suppliers_to_db(suppliers: list[dict[str, Any]], engine_db: Engine):
    """
    Adds a list of suppliers to the database.

    Args:
        suppliers (list[dict[str, Any]]): A list of dictionaries representing suppliers.
        engine_db (Engine): The SQLAlchemy engine object representing the database connection.

    Returns:
        None

    Raises:
        None
    """
    logger.info("Adding suppliers to database ...")
    with Session(engine_db) as session:
        for supplier in suppliers:
            # pprint(f"country_name={supplier['country_name']}")
            session.add(
                Supplier(
                    name=supplier["name"],
                    verification_mode=supplier["verified_type"],
                    sopi_level=supplier["sopi_level"],
                    country_name=supplier["country_name"],
                    years_as_gold_supplier=supplier["gold_supplier_year"],
                )
            )
        session.commit()


def add_products_to_db(products: list[dict[str, Any]], engine_db: Engine):
    """
    Adds a list of products to the database.

    Args:
        products (list[dict[str, Any]]): A list of dictionaries representing products.
        engine_db (Engine): The SQLAlchemy engine object representing the database connection.

    Returns:
        None

    Raises:
        None
    """
    logger.info("Adding products to database ...")
    with Session(engine_db) as session:
        for product in products:
            supplier = _related_supplier(session, supplied_by=product["supplied_by"])
            session.add(
                Product(
                    name=product["name"],
                    alibaba_guranteed=product["guaranteed_by_alibaba"],
                    certifications=product["certifications"],
                    minimum_to_order=product["minimum_to_order"],
                    ordered_or_sold=product["ordered_or_sold"],
                    supplier_id=supplier.id,
                    min_price=product["min_price"],
                    max_price=product["max_price"],
                )
            )
        session.commit()


def _related_supplier(current_session: Session, supplied_by: str):
    logger.info("Getting related supplier ...")
    query_statement = select(Supplier).where(Supplier.name == supplied_by)
    return current_session.exec(query_statement).all()[0]


if __name__ == "__main__":
    ...
