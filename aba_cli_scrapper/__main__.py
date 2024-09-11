import asyncio
import json
import os
import platform as pf
import sqlite3
import sys
from pathlib import Path
from typing import Optional


import click
import dotenv
import sqlalchemy
import typer
from click import MissingParameter, UsageError
from dotenv import load_dotenv
from loguru import logger
from rich import print as rprint
from rich.progress import (
	Progress,
	SpinnerColumn,
)
from sqlmodel import SQLModel
from trogon import tui
from typing_extensions import Annotated
import datahorse
import pandas as pd


from . import LOGURU_LEVEL
from .engine_and_database import (
	add_products_to_db,
	add_suppliers_to_db,
	create_db_engine,
	save_all_changes,
)
from .info_message import update_db_success_sqlite, update_db_with_success
from .scrape_from_disk import PageParser
from aba_cli_scrapper.proxies_providers import BrightDataProxyProvider, SyphoonProxyProvider
from .ascii import display_banner, get_current_version

load_dotenv()
logger.remove(0)
logger.add(sys.stderr, colorize=True, level=f"{LOGURU_LEVEL}")  # type: ignore
# display_banner()  # display banner for all commands


@tui(name="text-mode", command="aba-run")
@click.group()
def app():
	pass


app_t = typer.Typer(
	pretty_exceptions_enable=False,
)


@app_t.command()
def version():
	"""
	Display the version of the program
	"""
	rprint(f"[magenta]aba-cli-scrapper version:[/magenta] [blue]{get_current_version()}")


# @app_t.callback(invoke_without_command=True,name="--version", help="Display the version of the program",)
# def version():
# 	rprint(f"[magenta]aba-cli-scrapper version:[/magenta] [blue]{get_current_version()}")


def _db_url(credentials: dict = dict(), auto_fill: bool = False):
	"""
	Return a SQLAlchemy database URL based on the given credentials.

	If `auto_fill` is True, use the credentials from `db_credentials.json` if it exists
	and fill in any missing values from the provided `credentials`. If `db_credentials.json`
	does not exist, raise a UsageError.

	If `auto_fill` is False, use the provided `credentials` to create a new database URL
	and write it to `db_credentials.json`.
	"""
	if auto_fill is True:
		if Path("db_credentials.json").exists() is False:
			raise UsageError(
				"db_credentials.json is missing if you want to auto fill your mysql credentials you need to run `db-init` subcommand at least once with `--user`, `--password` and `--db-name` arguments."
			)
		with open("db_credentials.json", "r") as f:
			cred: dict = json.load(f)
			items = credentials.items()
			for item in items:
				if item[0] == "host" and item[1] not in ["localhost", None]:
					cred.update({"host": item[1]})
				elif item[0] == "port" and item[1] not in [3306, None]:
					cred.update({"port": item[1]})
				elif item[0] == "db_name" and item[1] not in [
					cred.get("db_name"),
					None,
				]:
					cred.update({"db_name": item[1]})
				elif item[0] == "user" and item[1] not in [
					cred.get("user"),
					None,
				]:
					cred.update({"user": item[1]})
				elif item[0] == "password" and item[1] not in [
					cred.get("password"),
					None,
				]:
					cred.update({"password": item[1]})
				else:
					continue
		return f"mysql+pymysql://{cred.get('user')}:{cred.get('password')}@{cred.get('host')}/{cred.get('db_name')}"

	else:
		cred = {
			"user": credentials.get("user"),
			"password": credentials.get("password"),
			"host": credentials.get("host"),
			"port": credentials.get("port"),
			"db_name": credentials.get("db_name"),
		}
		for key, value in cred.items():
			if value is None:
				raise MissingParameter(f"{key} is missing")
		with open("db_credentials.json", "w") as f:
			json.dump(cred, f)
		return f"mysql+pymysql://{cred.get('user')}:{cred.get('password')}@{cred.get('host')}/{cred.get('db_name')}"


@app_t.command()
def scraper(
	key_words: Annotated[str, typer.Argument(help="Keywords to search for on alibaba")] = "",
	html_folder: Annotated[
		Optional[str],
		typer.Option("--html-folder", "-hf", help="Folder to save the results"),
	] = None,
	sync_api: Annotated[
		Optional[bool],
		typer.Option("--sync-api", "-sa", help="wether to sync or not"),
	] = False,
	page_results: Annotated[
		int,
		typer.Option(
			"--page-results",
			"-pr",
			help="Number of results per page to scrape from alibaba 10 by defaults",
		),
	] = 10,
) -> None:
	"""
	Scrape with Bright-Data proxies rovider.
	"""
	display_banner()  # display banner for all commands
	save_in_folder = (
		key_words.strip().replace(" ", "_")
		if (html_folder is None and html_folder != "")
		else html_folder
	)
	if sync_api:
		BrightDataProxyProvider.sync_scraper(
			save_in=save_in_folder,
			key_words=key_words,
			page_results=page_results,
		)
	else:
		asyncio.run(
			BrightDataProxyProvider.async_scraper(
				save_in=save_in_folder, key_words=key_words, page_results=page_results
			)
		)


@app_t.command()
def syphoon_scraper(
	key_words: Annotated[str, typer.Argument(help="Keywords to search for on alibaba")] = "",
	html_folder: Annotated[
		Optional[str],
		typer.Option("--html-folder", "-hf", help="Folder to save the results"),
	] = None,
	sync_api: Annotated[
		Optional[bool],
		typer.Option("--sync-api", "-sa", help="wether to sync or not"),
	] = False,
	page_results: Annotated[
		int,
		typer.Option(
			"--page-results",
			"-pr",
			help="Number of results per page to scrape from alibaba 10 by defaults",
		),
	] = 10,
):
	"""
	Scrape with Syphoon proxies provider.
	"""
	display_banner()  # display banner for all commands
	save_in_folder = (
		key_words.strip().replace(" ", "_")
		if (html_folder is None and html_folder != "")
		else html_folder
	)
	if sync_api:
		SyphoonProxyProvider.sync_scraper(
			save_in=save_in_folder,
			key_words=key_words,
			page_results=page_results,
		)
	else:
		asyncio.run(
			SyphoonProxyProvider.async_scraper(
				save_in=save_in_folder, key_words=key_words, page_results=page_results
			)
		)


@app_t.command()
def db_update(
	kw_results: Annotated[
		Path,
		typer.Option(
			"--kw-results",
			"-kr",
			help="Folder where the html results are stored",
		),
	],
	db_engine: Annotated[
		Optional[str], typer.Argument(help="Name of database engine to use")
	] = "sqlite",
	filename: Annotated[
		Optional[str],
		typer.Option(
			"--filename",
			"-f",
			help="Name of the sqlite file(without any extensions) to update with news data",
		),
	] = None,
	host: Annotated[
		Optional[str],
		typer.Option(
			"--host",
			"-h",
			help="Host of the database engine",
		),
	] = "localhost",
	port: Annotated[
		Optional[int],
		typer.Option("--port", "-p", help="Port of the database engine"),
	] = 3306,
	user: Annotated[
		Optional[str],
		typer.Option(
			"--user",
			"-u",
			help="User of the database engine",
			show_default=False,
		),
	] = None,
	password: Annotated[
		Optional[str],
		typer.Option(
			"--password",
			"-pw",
			help="Password of the database engine",
			show_default=False,
		),
	] = None,
	db_name: Annotated[
		Optional[str],
		typer.Option(
			"--db-name",
			"-db",
			help="Database of the database engine",
			show_default=False,
		),
	] = None,
):
	"""Update a database with scraped products and suppliers data."""
	display_banner()  # display banner for all commands
	if db_engine not in ["sqlite", "mysql"]:
		raise MissingParameter("--engine should be sqlite or mysql")
	if db_engine == "sqlite" and filename is None:
		raise MissingParameter("--filename is required for sqlite engine")
	if db_engine != "sqlite" and filename is not None:
		raise MissingParameter("You don't need to specify --filename for non-sqlite engine")
	if db_engine == "mysql":
		db_url = _db_url(credentials=locals(), auto_fill=True)
		mysql_engine = create_db_engine(db_url=db_url)
		page_parser = PageParser(targeted_folder=kw_results.resolve())
		suppliers = page_parser.detected_suppliers()
		products = page_parser.detected_products()
		add_suppliers_to_db(suppliers=suppliers, engine_db=mysql_engine)
		add_products_to_db(products=products, engine_db=mysql_engine)
		save_all_changes(engine_db=mysql_engine, sql_model=SQLModel)
		update_db_with_success()
		return None
	if not kw_results.exists():
		raise UsageError(f"Folder {kw_results} does not exist")
	else:
		page_parser = PageParser(targeted_folder=kw_results)
		suppliers = page_parser.detected_suppliers()
		products = page_parser.detected_products()
		sqlite_engine = create_db_engine(db_name=filename)  # type: ignore
		add_suppliers_to_db(suppliers=suppliers, engine_db=sqlite_engine)
		add_products_to_db(products=products, engine_db=sqlite_engine)
		save_all_changes(engine_db=sqlite_engine, sql_model=SQLModel)
		update_db_success_sqlite(sqlite_file=filename)  # type: ignore


@app_t.command()
def db_init(
	engine: Annotated[str, typer.Argument(help="Name of database engine to use")] = "sqlite",
	sqlite_file: Annotated[
		Optional[str],
		typer.Option(
			"--sqlite-file",
			"-f",
			help="Name of the sqlite file to use (without any extensions)",
			show_default=False,
		),
	] = None,
	host: Annotated[
		Optional[str],
		typer.Option(
			"--host",
			"-h",
			help="Host of the database engine",
		),
	] = "localhost",
	port: Annotated[
		Optional[int],
		typer.Option("--port", "-p", help="Port of the database engine"),
	] = 3306,
	user: Annotated[
		Optional[str],
		typer.Option("--user", "-u", help="User of the database engine"),
	] = None,
	password: Annotated[
		Optional[str],
		typer.Option("--password", "-pw", help="Password of the database engine"),
	] = None,
	db_name: Annotated[
		Optional[str],
		typer.Option(
			"--db-name",
			"-db",
			help="Database of the database engine",
		),
	] = None,
	only_with: Annotated[
		Optional[bool],
		typer.Option(
			"--only-with",
			"-ow",
			help="set it to true if you just want to update some database crendentials but not all",
		),
	] = False,
):
	"""
	Create a new database sqlite/mysql with `<products>` and `<suppliers>` as tables in it.
	"""
	display_banner()  # display banner for all commands
	if engine not in ["sqlite", "mysql"]:
		raise MissingParameter("--engine should be sqlite or mysql")
	if engine == "sqlite" and sqlite_file is None:
		raise MissingParameter("--sqlite-file is required for sqlite engine")
	if engine != "sqlite" and sqlite_file is not None:
		raise MissingParameter("You dont need to specify --sqlite-file for non-sqlite engine")
	if engine == "mysql":
		if only_with:
			db_url = _db_url(credentials=locals(), auto_fill=True)
		else:
			db_url = _db_url(credentials=locals())
		mysql_engine = create_db_engine(db_url=db_url)
		try:
			save_all_changes(engine_db=mysql_engine, sql_model=SQLModel)
			rprint(
				f"[bold white]Database [magenta bold] {db_name} [/magenta bold] has been created succesfully :white_heavy_check_mark-emoji: ![/bold white]"
			)
		except sqlalchemy.exc.OperationalError as e:
			if "Unknown database" in str(e):
				rprint(
					f"[bold white blink] It's seems like you want to use mysql engine but you haven't created database: [magenta bold] `{db_name}` [/magenta bold] ![/bold white blink] create it first and then try again"
				)
			logger.error(f"Errors has occured: {e}")
	else:
		sqlite_engine = create_db_engine(db_name=sqlite_file)  # type: ignore
		save_all_changes(engine_db=sqlite_engine, sql_model=SQLModel)
		rprint(
			f"[bold white]Database [magenta bold] {sqlite_file}.sqlite [/magenta bold] has been created succesfully :white_heavy_check_mark-emoji: ![/bold white]"
		)


@app_t.command()
def export_as_csv(
	sqlite_file: Annotated[
		str,
		typer.Argument(
			help="take name of the sqlite file",
		),
	],
	to: Annotated[
		str,
		typer.Option(
			"--to",
			"-t",
			help="take name of the csv file",
		),
	],
):
	"""Exports a sqlite database as a csv file. A `FULL OUTER JOIN` operation will be used to join the two tables."""
	display_banner()  # display banner for all commands
	query = """
      SELECT Product.id as product_id,
      Product.name as product_name,
      Product.alibaba_guranteed as alibaba_guranteed,
      Product.minimum_to_order as minimum_to_order,
      Product.supplier_id as related_supplier_id,
      Product.certifications as certifications,
      Product.ordered_or_sold as ordered_or_sold,
      Product.product_score as product_score,
      Product.review_count  as review_count,
      Product.review_score as review_score,
      Product.shipping_time_score as shipping_time_score,
      Product.is_full_promotion as is_full_promotion,
      Product.is_customizable as is_customizable,
      Product.is_instant_order as is_instant_order,
      Product.trade_product  as trade_product,
      Product.min_price as min_price,
      Product.max_price as max_price,
      supplier.name as supplier_name ,
      supplier.verification_mode,
      supplier.sopi_level as sopi_level,
      supplier.country_name as country_name,
      supplier.years_as_gold_supplier as years_as_gold_supplier,
      supplier.supplier_service_score as supplier_service_score,
      supplier.id as supplier_id
      FROM Product
      JOIN Supplier ON Product.supplier_id = Supplier.id"""
	try:
		connector = sqlite3.connect(f"{sqlite_file}")
		df = pd.read_sql_query(query, connector)
		df.to_csv(
			f"{to}",
			index=True,
			encoding="utf-8",
			header=True,
			index_label="supplier_id",
		)
	except sqlite3.OperationalError as e:
		if pf.system() != "Windows":
			raise UsageError(f"{pf.system()} does not support <export-as-csv> command cause: {e}")
		raise UsageError(f"An error has occured with <{sqlite_file}>:  {e}")

	rprint(
		f"[bold white] {to} file has been created with success :white_heavy_check_mark-emoji: ![/bold white]"
	)


@app_t.command()
def set_api_key(
	api_key: Annotated[
		str,
		typer.Argument(
			help="take bright data api key you want to use",
		),
	],
	proxies_provider: Annotated[
		str,
		typer.Option(
			"--proxies-provider",
			"-pp",
			help="take proxies provider you want to use (i.e: Syphoon, Brightdata, etc.)",
		),
	],
) -> None:
	"""Sets your proxies provider api key could beBrightdata or Syphoon."""
	display_banner()  # display banner for all commands
	dotenv_file = dotenv.find_dotenv()
	dotenv.load_dotenv(dotenv_file)
	value = ""
	if proxies_provider == "brightdata":
		os.environ["BRIGHT_DATA_API_KEY"] = api_key
		value = "BRIGHT_DATA_API_KEY"
	elif proxies_provider == "syphoon":
		os.environ["SYPHOON_API_KEY"] = api_key
		value = "SYPHOON_API_KEY"
	else:
		return
	dotenv.set_key(dotenv_file, f"{value}", os.environ[f"{value}"])
	rprint(
		"[bold white]API key has been saved with success now you can use [magenta bold] `scraper` [/magenta bold] subcommand with async mode  :white_heavy_check_mark-emoji: ![/bold white]"
	)
	rprint(
		"[bold white]You can now use [magenta bold] `scraper` [/magenta bold]  subcommand with async mode with success :white_heavy_check_mark-emoji: ![/bold white]"
	)


@app_t.command()
def ai_agent(
	query: Annotated[
		str,
		typer.Argument(
			help="query that you want to ask to the ai agent",
		),
	],
	csv_file: Annotated[
		str,
		typer.Option(
			"--csv-file",
			"-f",
			help="take name of the csv file that you want to use to chat with the ai agent",
		),
	],
) -> None:
	"""Interact with a csv file provided by you to answer your queries."""
	df = datahorse.read(f"{csv_file}")
	if df is None:
		raise UsageError("An unexpected error has occured. May due to your csv file.")

	display_banner()  # display banner for all commands
	with Progress(
		SpinnerColumn(
			finished_text="[bold green]finished ✓[/bold green]",
		),
		# *Progress.get_default_columns(),
		transient=False,
	) as progress:
		task = progress.add_task(
			description="[green]Processing [blue][/blue] ...",
			start=False,
			total=100,
		)
		df_result = None
		try:
			progress.start_task(task)
			df_result = df.chat(  # type: ignore
				f"{query}"
				+ "return the result as a dataframe with only columns that are explicitly or implicitly asked."
			)  # type: ignore

		except Exception as e:
			raise UsageError(
				f"ai-agent : < An unexpected error has occured: {e}. \n Maybe i miss understood your query.change it a bit, or try the same again.>"
			)
		if type(df_result) is None:
			raise UsageError("An unexpected error has occured. May due to your query.")

		with open("buffer.csv", "w", encoding="utf-8") as output_file:
			df_result.to_csv(output_file)
		progress.advance(task, 100)
		progress.stop()
		os.system("rich buffer.csv --center")
		try:
			if pf.system() != "Windows":
				os.system("rm buffer.csv")
			else:
				os.system("del buffer.csv")
		except Exception as e:
			raise UsageError(
				f"ai-agent : << An unexpected error has occured: {e}. Remove the <buffer.csv> file manually. >>"
			)


typer_click_object = typer.main.get_command(app_t)

app.add_command(typer_click_object, "text-mode")

if __name__ == "__main__":
	app()
	app_t()
