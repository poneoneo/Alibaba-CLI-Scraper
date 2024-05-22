import json
from pathlib import Path
from typing import Optional
from click import MissingParameter
import typer
import sys
from web_scrapper import async_scrapper
import asyncio
from loguru import logger
from scrape_from_disk import PageParser
from engine_and_database import add_products_to_db, create_db_engine,save_all_changes,add_suppliers_to_db
from sqlmodel import SQLModel
from typing_extensions import Annotated
from rich import print as rprint

logger.remove(0)
logger.add(sys.stderr, colorize=True)

app = typer.Typer()

def _db_url(credentials:dict=dict(),auto_fill:bool=False):
    if auto_fill is True:
        if Path("db_credentials.json").exists() is False:
            raise FileNotFoundError("db_credentials.json is missing YOU NEED TO RUN `db-init` COMMAND FIRST !!")
        with open("db_credentials.json","r") as f:
            cred = json.load(f)
        return f"mysql+mysqldb://{cred.get('user')}:{cred.get('password')}@{cred.get('host')}/{cred.get('db_name')}"
    else:
        cred = {
            "user":credentials.get("user"),
            "password":credentials.get("password"),
            "host":credentials.get("host"),
            "port":credentials.get("port"),
            "db_name":credentials.get("db_name"),
        }   
        for key,value in cred.items():
            if value is None:
                raise MissingParameter(f"{key} is missing")
        with open("db_credentials.json","w") as f:
            json.dump(cred,f)
        return f"mysql+pymysql://{cred.get('user')}:{cred.get('password')}@{cred.get('host')}/{cred.get('db_name')}"  

@app.command()
def run_scrapper(
        key_words:Annotated[str,typer.Argument(help="Keywords to search")],
        html_folder:Annotated[Optional[str],typer.Option(help="Folder to save the results")]=None,
        ) -> None:
    """
    Runs the web scrapper to search for keywords and save the results in a specified folder.
    
    Args:
        key_words (str): The keywords to search for.
        html_folder (Optional[str], optional): The folder to save the results. Defaults to None.
    
    Returns:
        None
    
    Raises:
        None
    """
    if html_folder is None:
        save_in = key_words.strip().replace(" ","_")
    asyncio.run(async_scrapper(save_in=save_in,key_words=key_words))
    rprint("[bold white]Step :one:  is [bold green] done  :star: ! [/bold green] [/bold white]  ")
    rprint("[bold white blink]Scrapper has been completed [bold green]succesfully :white_heavy_check_mark-emoji: ![/bold green] [/bold white blink]")
    rprint("[bold white]Here we go to the step :two:   [/bold white]  ")
    rprint(f"[bold white blink]Now all pages results matching your keywords has been saved in [magenta]{html_folder}[/magenta] directory you can now append all products and suppliers into your database with [bold magenta]`db-update --kw-results {html_folder}`[/bold magenta] command[/bold white blink]")

@app.command()
def db_update(
    db_engine:Annotated[Optional[str],typer.Argument(help="Name of database engine to use")]='sqlite',
    kw_results=typer.Option(default=...,help="Folder where the html results are stored"),
    filename:Annotated[Optional[str],typer.Option(help="Name of the sqlite file(without any extensions) to update with news data",)]=None,
):
    """
    Updates the database with new products and their related suppliers.

    Args:
        db_engine (str, optional): The name of the database engine to use. Defaults to 'sqlite'.
        kw_results (str): The folder where the HTML results are stored.
        filename (str, optional): The name of the sqlite file (without any extensions) to update with news data. Defaults to None.

    Raises:
        MissingParameter: If the engine is not 'sqlite' or 'mysql', or if the filename is required for sqlite engine, or if the filename is specified for non-sqlite engine.

    Returns:
        None
    """
    if db_engine not in ["sqlite","mysql"]:
        raise MissingParameter("--engine should be sqlite or mysql")
    if db_engine == "sqlite" and filename is None:
        raise MissingParameter("--filename is required for sqlite engine" )
    if db_engine !="sqlite" and filename is not None:
        raise MissingParameter("You don't need to specify --filename for non-sqlite engine" )
    if db_engine == "mysql":
        db_url = _db_url(auto_fill=True)
        mysql_engine = create_db_engine(db_url=db_url)
        page_parser = PageParser(targeted_folder=kw_results)
        suppliers = page_parser.detected_suppliers()
        products = page_parser.detected_products()
        add_suppliers_to_db(suppliers=suppliers,engine_db=mysql_engine)
        add_products_to_db(products=products,engine_db=mysql_engine)
        save_all_changes(engine_db=mysql_engine,sql_model=SQLModel)
        rprint("[bold white]Step :three:  is [bold green] done  :star: ! [/bold green] [/bold white]")
        rprint("[bold white blink]Your database has been updated with new products and their related suppliers :white_heavy_check_mark-emoji: ![/bold white blink]")
        rprint("[bold white blink]Now you can do some amazing analysis woth your database for making your business more profitable :star: :star: ! [/bold white blink]")
     
    else:
        page_parser = PageParser(targeted_folder=kw_results)
        suppliers = page_parser.detected_suppliers()
        products = page_parser.detected_products()
        sqlite_engine = create_db_engine(db_name=filename) # type: ignore
        add_suppliers_to_db(suppliers=suppliers,engine_db=sqlite_engine)
        add_products_to_db(products=products,engine_db=sqlite_engine)
        save_all_changes(engine_db=sqlite_engine,sql_model=SQLModel)
        rprint(f"[bold white] [magenta bold] {filename}.sqlite [/magenta bold] file has been updated succesfully  with new products and their related suppliers :white_heavy_check_mark-emoji: ![/bold white]")
        rprint("[bold white]Step :three:  is [bold green] done  :star: ! [/bold green] [/bold white]  ")
        rprint("[bold white blink]Now you can do some amazing analysis with your database for making your business more profitable :star: :star: ! [/bold white blink]")


@app.command()
def db_init(
        engine:Annotated[str,typer.Argument(help="Name of database engine to use")]='sqlite',
        sqlite_file:Annotated[Optional[str],typer.Option(help="Name of the sqlite file to use (without any extensions)",show_default=False)]=None,
        host:Annotated[Optional[str],typer.Option(help="Host of the database engine",)]="localhost",
        port:Annotated[Optional[int],typer.Option(help="Port of the database engine")]=3306,
        user:Annotated[Optional[str],typer.Option(help="User of the database engine",show_default=False)]=None,
        password:Annotated[Optional[str],typer.Option(help="Password of the database engine",show_default=False)]=None,
        db_name:Annotated[Optional[str],typer.Option(help="Database of the database engine",show_default=False)]=None,
  ):
    """
    Initializes a database using the specified engine.

    Args:
        engine (str): The name of the database engine to use. Defaults to 'sqlite'.
        sqlite_file (Optional[str]): The name of the sqlite file to use (without any extensions).
            Required for 'sqlite' engine.
        host (Optional[str]): The host of the database engine. Defaults to 'localhost'.
        port (Optional[int]): The port of the database engine.
        user (Optional[str]): The user of the database engine.
        password (Optional[str]): The password of the database engine.
        db_name (Optional[str]): The database of the database engine.

    Raises:
        MissingParameter: If the engine is not 'sqlite' or 'mysql', or if the filename is required for sqlite engine,
            or if the filename is specified for non-sqlite engine.

    Returns:
        None

    This function initializes a database using the specified engine. It checks the validity of the engine and the
    required parameters. If the engine is 'sqlite', it creates a sqlite database file with the specified name. If the
    engine is 'mysql', it creates a mysql database using the specified host, port, user, password, and database name.
    After creating the database, it saves the changes to the database using the `save_all_changes` function. Finally,
    it prints a success message indicating the creation of the database.
    """
    if engine not in ["sqlite","mysql"]:
        raise MissingParameter("--engine should be sqlite or mysql")
    if engine == "sqlite" and sqlite_file is None:
        raise MissingParameter("--sqlite-file is required for sqlite engine" )
    if engine !="sqlite" and sqlite_file is not None:
        raise MissingParameter("You dont need to specify --sqlite-file for non-sqlite engine")
    if engine == "mysql":
        db_url = _db_url(credentials=locals())
        mysql_engine = create_db_engine(db_url=db_url)
        save_all_changes(engine_db=mysql_engine,sql_model=SQLModel)
        rprint(f"[bold white]Database [magenta bold] {db_name} [/magenta bold] has been created succesfully :white_heavy_check_mark-emoji: ![/bold white]")
    else:
        sqlite_engine = create_db_engine(db_name=sqlite_file) # type: ignore
        save_all_changes(engine_db=sqlite_engine,sql_model=SQLModel)
        rprint(f"[bold white]Database [magenta bold] {sqlite_file}.sqlite [/magenta bold] file has been created succesfully :white_heavy_check_mark-emoji: ![bold white]")
              
if __name__ == "__main__":
    app()