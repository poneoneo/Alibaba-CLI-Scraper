from aba_cli_scrapper.commands import app, app_t
import typer

typer_click_object = typer.main.get_command(app_t)
app.add_command(typer_click_object, "")
