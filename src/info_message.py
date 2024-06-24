from rich import print as rprint


def run_scrapper_with_success(folder_name: str):
    rprint(
        "[bold white]Step :one:  is [bold green] done  :star: ! [/bold green] [/bold white]  "
    )
    rprint(
        "[bold white blink]Scrapper has been completed [bold green]succesfully :white_heavy_check_mark-emoji: ![/bold green] [/bold white blink]"
    )
    rprint("[bold white]Here we go to the step :two:   [/bold white]  ")
    rprint(
        f"[bold white blink]Now all pages results matching your keywords has been saved in [magenta]{folder_name}[/magenta] directory you can now add all products and suppliers into your database with [bold magenta]`db-update --kw-results {folder_name}`[/bold magenta] command[/bold white blink]"
    )


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
