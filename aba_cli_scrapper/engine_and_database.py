from typing import Sequence

from click import UsageError
from loguru import logger
from MySQLdb import OperationalError as MySQLdbOperationalError
from rich.progress import (
    BarColumn,
    Progress,
    SpinnerColumn,
    TaskProgressColumn,
    TextColumn,
    TimeElapsedColumn,
)
from sqlalchemy.engine import Engine
from sqlalchemy.exc import IntegrityError, OperationalError
from sqlmodel import Session, SQLModel, create_engine, select  # noqa: F401

from aba_cli_scrapper.typed_datas import ProductDict, SupplierDict

from .models import Product, Supplier  # noqa: F401


def create_db_engine(db_name: str = "", db_url: str = ""):
    db_url = db_url if db_url else f"sqlite:///{db_name}.sqlite"
    return create_engine(db_url)


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
    except MySQLdbOperationalError as e:
        logger.error(f"Errors has occured: {e}")
        raise UsageError(
            f"Something went wrong an unexpected error has occured:{e}"
        ) from e


def add_suppliers_to_db(suppliers: Sequence[SupplierDict], engine_db: Engine):
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
        added = set()
        with Progress(
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TaskProgressColumn(),
            TimeElapsedColumn(),
            transient=True,
        ) as progress:
            adder_supp = progress.add_task(
                description="Adding suppliers to database ..."
            )
            for supplier in suppliers:
                # pprint(f"country_name={supplier['country_name']}")
                if supplier["name"] in added:
                    continue
                session.add(
                    Supplier(
                        name=supplier["name"],
                        verification_mode=supplier["verified_type"],
                        sopi_level=supplier["sopi_level"],
                        country_name=supplier["country_name"],
                        years_as_gold_supplier=supplier["gold_supplier_year"],
                        supplier_service_score=supplier["supplier_service_score"],
                    )
                )
                added.add(supplier["name"])
                try:
                    session.commit()
                    progress.update(adder_supp, advance=100 / len(suppliers))
                except OperationalError as e:
                    if "no such table" in str(e):
                        raise UsageError(
                            "Your database must be initialized before if you want to update it. instead run :  `aba-run db-init sqlite sqlite-file <your_sqlite_db_file_name>`"
                        ) from e
                    raise UsageError(
                        f"Something went wrong an unexpected error has occured:{e}"
                    ) from e
                except IntegrityError as e:
                    raise UsageError(
                        "Seems like you are trying to update a database which has already been updated ! Instead initialize a new one and update it with: `aba-run db-update sqlite --sqlite-file <new_sqlite_db_file_name>` "
                    ) from e


def add_products_to_db(products: Sequence[ProductDict], engine_db: Engine):
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
        added = set()
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TaskProgressColumn(),
            TimeElapsedColumn(),
            transient=True,
        ) as progress:
            try:
                add_prods = progress.add_task(
                    description="Adding products to database ..."
                )
                for product in products:
                    if product["name"] in added:
                        continue
                    supplier = _related_supplier(
                        session, supplied_by=product["supplied_by"]
                    )
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
                            trade_product=product["trade_product"],
                            review_count=product["review_count"],
                            review_score=product["review_score"],
                            product_score=product["product_score"],
                            shipping_time_score=product["shipping_time_score"],
                            is_instant_order=product["instant_order"],
                            is_customizable=product["customizable"],
                            is_full_promotion=product["is_full_promotion"],
                        )
                    )
                    added.add(product["name"])
                    session.commit()
                    progress.update(add_prods, advance=100 / len(products))
            except OperationalError as e:
                logger.error(f"Errors has occured: {e}")
                if "no such table" in str(e):
                    raise UsageError(
                        "Your database must be initialized first run : aba db-init --help to know more "
                    ) from e
                raise UsageError(
                    f"Something went wrong an unexpected error has occured:{e}"
                ) from e


def _related_supplier(current_session: Session, supplied_by: str):
    logger.info("Getting related supplier ...")
    query_statement = select(Supplier).where(Supplier.name == supplied_by)
    return current_session.exec(query_statement).all()[0]


if __name__ == "__main__":
    ...
