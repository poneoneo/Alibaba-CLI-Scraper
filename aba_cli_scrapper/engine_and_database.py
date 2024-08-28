from typing import Sequence

from click import UsageError
from loguru import logger
from pymysql import OperationalError as MySQLdbOperationalError
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
	"""This function creates a new database engine using SQLAlchemy's create_engine method.

	The function takes two arguments: db_name and db_url. db_name is the name of the database
	and db_url is the connection string for the database. If db_url is not provided, the
	function will use a default connection string based on db_name.

	The function returns a new database engine object.

	:param db_name: The name of the database.
	:type db_name: str
	:param db_url: The connection string for the database.
	:type db_url: str
	:return: A new database engine object.
	:rtype: sqlalchemy.engine.Engine
	"""
	db_url = db_url if db_url else f"sqlite:///{db_name}.sqlite"
	return create_engine(db_url)


def save_all_changes(
	engine_db: Engine,
	sql_model,
):
	"""Save all changes to the database.

	This function takes two arguments: engine_db and sql_model. engine_db is the database
	engine object created by create_engine method of SQLAlchemy. sql_model is the
	SQLModel object which is used to access the metadata of the database.

	The function will try to create all tables in the database by calling
	create_all() method of the metadata object. If any error occur during the
	process, it will raise a UsageError with the error message.

	:param engine_db: The database engine object.
	:type engine_db: sqlalchemy.engine.Engine
	:param sql_model: The SQLModel object.
	:type sql_model: sqlmodel.main.SQLModel
	:raises UsageError: If any error occur during the process of creating tables.
	"""
	logger.info("Saving all changes ...")
	try:
		sql_model.metadata.create_all(engine_db)
	except MySQLdbOperationalError as e:
		logger.error(f"Errors has occured: {e}")
		raise UsageError(f"Something went wrong an unexpected error has occured:{e}") from e


def add_suppliers_to_db(suppliers: Sequence[SupplierDict], engine_db: Engine):
	"""
	Add suppliers to the database.

	This function takes two arguments: suppliers and engine_db. suppliers is a list of dictionaries
	containing information about the suppliers. engine_db is the database engine object created by
	create_engine method of SQLAlchemy.

	The function will iterate over the list of suppliers and add each one to the database using the
	Supplier model. If any error occur during the process, it will raise a UsageError with the
	error message.

	:param suppliers: A list of dictionaries containing information about the suppliers.
	:type suppliers: Sequence[SupplierDict]
	:param engine_db: The database engine object.
	:type engine_db: sqlalchemy.engine.Engine
	:raises UsageError: If any error occur during the process of adding suppliers.
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
			adder_supp = progress.add_task(description="Adding suppliers to database ...")
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
	Add products to the database.

	This function takes two arguments: products and engine_db. products is a list of dictionaries
	containing information about the products. engine_db is the database engine object created by
	create_engine method of SQLAlchemy.

	The function will iterate over the list of products and add each one to the database using the
	Product model. If any error occur during the process, it will raise a UsageError with the
	error message.

	:param products: A list of dictionaries containing information about the products.
	:type products: Sequence[ProductDict]
	:param engine_db: The database engine object.
	:type engine_db: sqlalchemy.engine.Engine
	:raises UsageError: If any error occur during the process of adding products.
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
				add_prods = progress.add_task(description="Adding products to database ...")
				for product in products:
					if product["name"] in added:
						continue
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
				raise UsageError(f"Something went wrong an unexpected error has occured:{e}") from e


def _related_supplier(current_session: Session, supplied_by: str):
	"""
	Retrieve the supplier related to the given product.

	:param current_session: The database session object.
	:type current_session: sqlalchemy.orm.Session
	:param supplied_by: The name of the supplier.
	:type supplied_by: str
	:return: A Supplier object.
	:rtype: Supplier
	"""
	logger.info("Getting related supplier ...")
	query_statement = select(Supplier).where(Supplier.name == supplied_by)
	return current_session.exec(query_statement).all()[0]


if __name__ == "__main__":
	...
