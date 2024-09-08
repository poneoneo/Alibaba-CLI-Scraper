import pytest
from aba_cli_scrapper.__main__ import app_t
from typer.testing import CliRunner
import socket
from pathlib import Path
import shutil
import subprocess
import os


html_test_folder = Path("tests/Air_fryers").resolve()
runner = CliRunner()
Path("fa.sqlite").unlink()


####### Test Mysql database######
def test_db_init_mysql_database():
	"""
	Test db-init command with mysql engine and given filename. Since this test schemas has not been created yet, command must inform user to create it.
	"""

	result = runner.invoke(
		app_t, ["db-init", "mysql", "-u", "Oneal_Dev", "-pw", "0nealDev!te", "-db", "test"]
	)
	assert result.exit_code == 0
	assert "It's seems like you want to use mysql engine" in result.stdout


def test_db_init_mysql_database_auto_fill():
	"""
	Test db-init mysql engine with auto-fill case
	"""

	result = runner.invoke(app_t, ["db-init", "mysql", "-db", "air_fryers", "-ow"])
	assert result.exit_code == 0
	assert "air_fryers  has been created succesfully" in result.stdout


def test_db_update_mysql_database_already_exists():
	"""
	Test db-update command with mysql engine and given db that already exists.
	"""
	result = runner.invoke(app_t, ["db-update", "-db", "air_fryers", "-kr", html_test_folder])
	assert result.exit_code == 2

	####### Test sqlite database######


def test_db_init_sqlite_file():
	"""
	Test db-init command with sqlite engine and given filename
	"""

	result = runner.invoke(app_t, ["db-init", "-f", "fa"])
	assert result.exit_code == 0
	assert "Database  fa.sqlite  has been created succesfully" in result.stdout


def test_db_update_sqlite_file():
	"""
	Test db-update command with sqlite engine.
	"""
	result = runner.invoke(app_t, ["db-update", "-f", "fa", "-kr", html_test_folder])
	assert result.exit_code == 0


def test_db_update_sqlite_file_already_exists():
	"""
	Test db-update command with sqlite engine and given filename that already exists.
	"""
	result = runner.invoke(app_t, ["db-update", "-f", "fa", "-kr", html_test_folder])
	assert result.exit_code == 2

	####### Test export-as-csv ######


def test_export_as_csv():
	result = runner.invoke(app_t, ["export-as-csv", "fa.sqlite", "-t", "facsv.csv"])
	assert result.exit_code == 0
	assert "facsv.csv file has been created with success" in result.stdout

	####### Test ai-agent ######


def test_ai_gent():
	result = runner.invoke(app_t, ["ai-agent", "get all suppliers", "-f", "facsv.csv"])
	assert result.exit_code == 0

	####### Test db-update with not found directory ######


@pytest.mark.filterwarnings("ignore::pytest.PytestUnraisableExceptionWarning")
@pytest.mark.filterwarnings("ignore:: RuntimeWarning")
def test_db_update_with_not_found_directory():
	result = runner.invoke(app_t, ["db-update", "-f", "fa", "-kr", "./Foo_Bar"])
	assert result.exit_code == 2

	####### Test sync scraper with bright data ######


@pytest.mark.filterwarnings("ignore:: RuntimeWarning")
def test_sync_scraper_with_bright_data():
	my_env = os.environ.copy()
	proc = subprocess.Popen(
		["aba-run", "scraper", "pc dell", "-pr", "2", "-sa"],
		shell=True,
		env=my_env,
		stdout=subprocess.PIPE,
	)
	out = proc.stdout
	assert "Done" in out.read().decode("utf-8")
	assert Path("pc_dell/").exists() is True
	assert len(list(Path("pc_dell").glob("*.html"))) == 2
	shutil.rmtree("pc_dell/")

	####### Test sync scraper with syphoon ######


@pytest.mark.filterwarnings("ignore:: RuntimeWarning")
def test_sync_scraper_with_syphoon():
	my_env = os.environ.copy()
	proc = subprocess.Popen(
		["aba-run", "syphoon-scraper", "pc dell", "-pr", "2", "-sa", "-hf", "pc_dell_custom"],
		shell=True,
		env=my_env,
		stdout=subprocess.PIPE,
	)
	out = proc.stdout
	assert "Done" in out.read().decode("utf-8")
	assert Path("pc_dell_custom/").exists() is True
	assert len(list(Path("pc_dell_custom/").glob("*.html"))) == 2
	shutil.rmtree("pc_dell_custom/")

	####### Test async scraper with bright data ######


@pytest.mark.filterwarnings("ignore:: RuntimeWarning")
def test_async_scraper_with_bright_data():
	my_env = os.environ.copy()
	proc = subprocess.Popen(
		["aba-run", "scraper", "pc dell", "-pr", "2"],
		shell=True,
		env=my_env,
		stdout=subprocess.PIPE,
	)
	out = proc.stdout
	assert "Done" in out.read().decode("utf-8")
	assert Path("pc_dell/").exists() is True
	assert len(list(Path("pc_dell/").glob("*.html"))) == 2
	shutil.rmtree("pc_dell/")

	####### Test async scraper with syphoon ######


@pytest.mark.filterwarnings("ignore:: RuntimeWarning")
def test_async_scraper_with_syphoon():
	my_env = os.environ.copy()
	proc = subprocess.Popen(
		[
			"aba-run",
			"syphoon-scraper",
			"pc dell",
			"-pr",
			"2",
		],
		shell=True,
		env=my_env,
		stdout=subprocess.PIPE,
	)
	out = proc.stdout
	assert "Done" in out.read().decode("utf-8")
	assert Path("pc_dell/").exists() is True
	assert len(list(Path("pc_dell/").glob("*.html"))) == 2
	shutil.rmtree("pc_dell/")

	####### Test scraper with no internet ######


class block_network(socket.socket):
	def __init__(self, *args, **kwargs):
		raise Exception("Network call blocked")


def test_scraper_no_internet():
	socket.socket = block_network
	result = runner.invoke(app_t, ["scraper", "pc dell", "-pr", "3"])
	assert result.exit_code == 1
