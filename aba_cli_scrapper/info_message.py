from rich import print as rprint


def run_scrapper_with_success(folder_name: str):
    rprint(
        "[bold white]Step :one:  is [bold green] done  :star: ! [/bold green] [/bold white]  "
    )
    rprint(
        "[bold white blink]Scrapper has been completed [bold green]succesfully :white_heavy_check_mark-emoji: ![/bold green] [/bold white blink]"
    )
    rprint("""[bold white]Here we go to the step :two:   [/bold white]
        initialize your database with [bold magenta blink]python src/app.py db-init --engine mysql --user your_username --password your_password --db-name alibaba_products[/bold magenta blink] command(for mysql engine) or [bold magenta blink]python src/app.py db-init --engine sqlite --sqlite-file sqlite_file_name(without any extensions) [/bold magenta blink] command(for sqlite engine)...""")
    # rprint(
    #     f"""[bold white ]Now all pages results matching your keywords has been saved in [magenta]{folder_name}[/magenta] now if is still not the case you must to initialize your database with [bold magenta blink]
    #     `python src/app.py db-init --engine mysql --user your_username --password your_password --db-name alibaba_products`[/bold magenta blink] command(for mysql engine).
    #     Or `python src/app.py db-init --engine sqlite --sqlite-file sqlite_file_name(without any extensions)` command(for sqlite engine). As soon as you have done that, you can update all thoses new scraped products and suppliers inside your database with [bold magenta blink]`python src/app.py db-update --db-engine mysql --kw-results {folder_name} command (for sqlite engine)`[/bold magenta blink] or [bold magenta blink]`python src/app.py db-update --db-engine sqlite --kw-results bike_results --filename {folder_name}`[/bold magenta blink]..."""
    # )


def update_db_with_success():
    rprint(
        "[bold white]Step :three:  is [bold green] done  :star: ! [/bold green] [/bold white]"
    )
    rprint(
        "[bold white blink]Your database has been updated with new products and their related suppliers :white_heavy_check_mark-emoji: ![/bold white blink]"
    )
    rprint(
        "[bold white blink]Now you can do some amazing analysis woth your database for making your business more profitable :star: :star: ! [/bold white blink]"
    )


def update_db_success_sqlite(sqlite_file: str):
    rprint(
        f"[bold white] [magenta bold] {sqlite_file}.sqlite [/magenta bold] file has been updated succesfully  with new products and their related suppliers :white_heavy_check_mark-emoji: ![/bold white]"
    )
    rprint(
        "[bold white]Step :three:  is [bold green] done  :star: ! [/bold green] [/bold white]  "
    )
    rprint(
        "[bold white blink]Now you can do some amazing analysis with your database for making your business more profitable :star: :star: ! [/bold white blink]"
    )
