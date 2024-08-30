from faker import Faker
import pytest
from aba_cli_scrapper.__main__ import app_t
from typer.testing import CliRunner
import socket
import sys


class block_network(socket.socket):
    def __init__(self, *args, **kwargs):
        raise Exception("Network call blocked")



runner = CliRunner()
def test_db_init_sqlite_file():
	"""
	Test db-init command with sqlite engine and given filename
	"""

	result = runner.invoke(app_t, ["db-init", "-f", "fa"])
	assert result.exit_code == 0
	assert "Database  fa.sqlite  has been created succesfully" in result.stdout


def test_db_init_mysql_database():
	"""
	Test db-init command with mysql engine and given filename. Since this test schemas has not been created yet, command must inform user to create it.
	"""

	result = runner.invoke(
		app_t, ["db-init", "mysql", "-u", "Oneal_Dev", "-pw", "0nealDev!te", "-db", "test"]
	)
	assert result.exit_code == 0
	assert "create it first and then try again" in result.stdout

def test_db_init_mysql_database_auto_fill():
	"""
	Test db-init mysql engine with auto-fill case
	"""

	result = runner.invoke(
		app_t, ["db-init", "mysql", "-db", "air_fryers","-ow"]
	)
	assert result.exit_code == 0
	assert "air_fryers  has been created succesfully" in result.stdout


def test_db_update_sqlite_file_already_exists():
	"""
	Test db-update command with sqlite engine and given filename that already exists.
	"""
	result = runner.invoke(app_t, ["db-update", "-f", "fa", "-kr", "./Air_fryers"])
	assert result.exit_code == 2


def test_db_update_mysql_database_already_exists():
	"""
	Test db-update command with mysql engine and given db that already exists.
	"""
	result = runner.invoke(app_t, ["db-update", "-db", "air_fryers", "-kr", "./Air_fryers"])
	assert result.exit_code == 2


def test_export_as_csv():
	result = runner.invoke(app_t, ["export-as-csv", "fa.sqlite", "-t", "facsv.csv"])
	assert result.exit_code == 0
	assert "facsv.csv file has been created with success" in result.stdout


def test_ai_gent():
	result = runner.invoke(app_t, ["ai-agent", "get all suppliers", "-f", "facsv.csv"])
	assert result.exit_code == 0


def test_scraper_no_internet():
	socket.socket = block_network
	result =  runner.invoke(app_t, ["scraper", "pc dell", "-pr", "3"])
	assert result.exit_code == 1

@pytest.mark.filterwarnings("ignore::pytest.PytestUnraisableExceptionWarning")
@pytest.mark.filterwarnings("ignore:: RuntimeWarning")
def test_db_update_with_not_found_directory():
	result = runner.invoke(app_t, ["db-update", "-f", "fa", "-kr", "./Foo_Bar"])
	assert result.exit_code == 2

def test_db_update_sqlite_file_successfully():
	fake = Faker()
	sqlite_filename = fake.first_name()[:3]
	runner.invoke(app_t, ["db-init", "-f", f"{sqlite_filename}"])
	result = runner.invoke(app_t, ["db-update", "-f", f"{sqlite_filename}","-kr","./Air_fryers"])
	assert f"{sqlite_filename}.sqlite  file has been updated succesfully" in result.stdout





