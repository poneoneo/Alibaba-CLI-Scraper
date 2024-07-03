import asyncio
import json
import os
import sys
from pathlib import Path
from typing import Optional

import sqlalchemy
import typer
from click import MissingParameter
from dotenv import load_dotenv
from .engine_and_database import (
    add_products_to_db,
    add_suppliers_to_db,
    create_db_engine,
    save_all_changes,
)
from .info_message import update_db_success_sqlite, update_db_with_success
from loguru import logger
from rich import print as rprint
from .scrape_from_disk import PageParser
from sqlmodel import SQLModel
from typing_extensions import Annotated
from .web_scrapper import async_scrapper, sync_scrapper

load_dotenv()

logger.remove(0)
logger.add(sys.stderr, colorize=True, level=os.environ.get("LOGURU_LEVEL", ""))

app = typer.Typer(pretty_exceptions_enable=False)


def _db_url(credentials: dict = dict(), auto_fill: bool = False):
    if auto_fill is True:
        if Path("db_credentials.json").exists() is False:
            raise FileNotFoundError(
                "db_credentials.json is missing YOU NEED TO RUN `db-init` COMMAND FIRST !!"
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
                elif item[0] == "user" and item[1] not in [cred.get("user"), None]:
                    cred.update({"user": item[1]})
                elif item[0] == "password" and item[1] not in [
                    cred.get("password"),
                    None,
                ]:
                    cred.update({"password": item[1]})
                else:
                    continue
        return f"mysql+mysqldb://{cred.get('user')}:{cred.get('password')}@{cred.get('host')}/{cred.get('db_name')}"

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
        return f"mysql+mysqldb://{cred.get('user')}:{cred.get('password')}@{cred.get('host')}/{cred.get('db_name')}"


@app.command()
def run_scrapper(
    key_words: Annotated[str, typer.Argument(help="Keywords to search")],
    html_folder: Annotated[
        Optional[str], typer.Option(help="Folder to save the results")
    ] = None,
    sync_api: Annotated[
        Optional[bool], typer.Option(help="wether to sync or not",default=False)
    ] = False,
) -> None:
    """
    Runs the web scrapper and loking for products and related suppliers infos based on provided keywords, then save the results in a specified folder by default this folder is named with the keywords that was provided and could attached with '_' if there are spaces in the keywords'.

    Args:
        key_words (str): The keywords to search for.
        html_folder (Optional[str], optional): The folder to save the results. Defaults to None.

    Returns:
        None

    Raises:
        None
    """

    save_in_folder = (
        key_words.strip().replace(" ", "_")
        if (html_folder is None and html_folder != "")
        else html_folder
    )
    if sync_api:
        sync_scrapper(save_in=save_in_folder, key_words=key_words)
    else:
        asyncio.run(async_scrapper(save_in=save_in_folder, key_words=key_words))


@app.command()
def db_update(
    db_engine: Annotated[
        Optional[str], typer.Argument(help="Name of database engine to use")
    ] = "sqlite",
    kw_results=typer.Option(
        default=..., help="Folder where the html results are stored"
    ),
    filename: Annotated[
        Optional[str],
        typer.Option(
            help="Name of the sqlite file(without any extensions) to update with news data",
        ),
    ] = None,
    host: Annotated[
        Optional[str],
        typer.Option(
            help="Host of the database engine",
        ),
    ] = "localhost",
    port: Annotated[
        Optional[int], typer.Option(help="Port of the database engine")
    ] = 3306,
    user: Annotated[
        Optional[str],
        typer.Option(help="User of the database engine", show_default=False),
    ] = None,
    password: Annotated[
        Optional[str],
        typer.Option(help="Password of the database engine", show_default=False),
    ] = None,
    db_name: Annotated[
        Optional[str],
        typer.Option(help="Database of the database engine", show_default=False),
    ] = None,
):
    """
    Updates the database with new products and their related suppliers.
    Raises:
        MissingParameter: If the engine is not 'sqlite' or 'mysql', or if the filename is required for sqlite engine, or if the filename is specified for non-sqlite engine.

    Returns:
        None
    """
    if db_engine not in ["sqlite", "mysql"]:
        raise MissingParameter("--engine should be sqlite or mysql")
    if db_engine == "sqlite" and filename is None:
        raise MissingParameter("--filename is required for sqlite engine")
    if db_engine != "sqlite" and filename is not None:
        raise MissingParameter(
            "You don't need to specify --filename for non-sqlite engine"
        )
    if db_engine == "mysql":
        db_url = _db_url(credentials=locals(), auto_fill=True)
        mysql_engine = create_db_engine(db_url=db_url)
        page_parser = PageParser(targeted_folder=kw_results)
        suppliers = page_parser.detected_suppliers()
        products = page_parser.detected_products()
        add_suppliers_to_db(suppliers=suppliers, engine_db=mysql_engine)
        add_products_to_db(products=products, engine_db=mysql_engine)
        save_all_changes(engine_db=mysql_engine, sql_model=SQLModel)
        update_db_with_success()

    else:
        page_parser = PageParser(targeted_folder=kw_results)
        suppliers = page_parser.detected_suppliers()
        products = page_parser.detected_products()
        sqlite_engine = create_db_engine(db_name=filename)  # type: ignore
        add_suppliers_to_db(suppliers=suppliers, engine_db=sqlite_engine)
        add_products_to_db(products=products, engine_db=sqlite_engine)
        save_all_changes(engine_db=sqlite_engine, sql_model=SQLModel)
        update_db_success_sqlite(sqlite_file=filename)  # type: ignore


@app.command()
def db_init(
    engine: Annotated[
        str, typer.Argument(help="Name of database engine to use")
    ] = "sqlite",
    sqlite_file: Annotated[
        Optional[str],
        typer.Option(
            help="Name of the sqlite file to use (without any extensions)",
            show_default=False,
        ),
    ] = None,
    host: Annotated[
        Optional[str],
        typer.Option(
            help="Host of the database engine",
        ),
    ] = "localhost",
    port: Annotated[
        Optional[int], typer.Option(help="Port of the database engine")
    ] = 3306,
    user: Annotated[
        Optional[str],
        typer.Option(help="User of the database engine"),
    ] = None,
    password: Annotated[
        Optional[str],
        typer.Option(help="Password of the database engine"),
    ] = None,
    db_name: Annotated[
        Optional[str],
        typer.Option(help="Database of the database engine", ),
    ] = None,
    only_with: Annotated[
        Optional[bool],
        typer.Option(
            help="set it to true if you just want to update some database crendentials but not all",
        ),
    ] = False
):
    """
    Initializes a database using the specified engine.

    Raises:
        MissingParameter: If the engine is not 'sqlite' or 'mysql', or if the filename is required for sqlite engine,
            or if the filename is specified for non-sqlite engine.


    This function initializes a database using the specified engine. It checks the validity of the engine and the
    required parameters. If the engine is 'sqlite', it creates a sqlite database file with the specified name. If the
    engine is 'mysql', it creates a mysql database using the specified host, port, user, password, and database name.
    After creating the database, it saves the changes to the database. Finally,
    it prints a success message indicating the creation of the database.
    """
    if engine not in ["sqlite", "mysql"]:
        raise MissingParameter("--engine should be sqlite or mysql")
    if engine == "sqlite" and sqlite_file is None:
        raise MissingParameter("--sqlite-file is required for sqlite engine")
    if engine != "sqlite" and sqlite_file is not None:
        raise MissingParameter(
            "You dont need to specify --sqlite-file for non-sqlite engine"
        )
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


if __name__ == "__main__":
    app()
