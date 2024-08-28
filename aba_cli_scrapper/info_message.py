from rich import print as rprint


def run_scrapper_with_success(folder_name: str):
	"""
	Print a success message after running the scrapper with success.
	"""

	rprint(
		"[bold white]Step :one:  [bold green] Done  :star::white_heavy_check_mark-emoji: ! [/bold green] [/bold white]  "
	)


def update_db_with_success():
	"""
	Print a success message after updating the database with new data.
	"""
	rprint("[bold white]Step :three:  is [bold green] done  :star: ! [/bold green] [/bold white]")
	rprint(
		"[bold white blink]Your database has been updated with new products and their related suppliers :white_heavy_check_mark-emoji: ![/bold white blink]"
	)
	rprint(
		"[bold white]Now you can do some amazing analysis with your database for making your business more profitable :star: :star: ! [/bold white ]"
	)


def update_db_success_sqlite(sqlite_file: str):
	"""Print a success message when the database has been updated with new products and suppliers."""
	rprint(
		f"[bold white][magenta bold]{sqlite_file}.sqlite [/magenta bold] file has been updated succesfully  with new products and their related suppliers :white_heavy_check_mark-emoji: ![/bold white]"
	)
	rprint("[bold white]Step :three:  is [bold green] done  :star: ! [/bold green] [/bold white]  ")
	rprint(
		"[bold white ]Now you can do some amazing analysis with your database for making your business more profitable :star: :star: ! [/bold white ]"
	)
