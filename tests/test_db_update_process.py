import pytest
from aba_cli_scrapper.scrape_from_disk import PageParser
from pathlib import Path

html_test_folder = Path("tests/Air_fryers").resolve()
print(html_test_folder)


@pytest.mark.filterwarnings("ignore::pytest.PytestUnraisableExceptionWarning")
@pytest.mark.filterwarnings("ignore:: RuntimeWarning")
def test_count_suppliers_and_products():
	# assert "dfgfg" == html_test_folder
	page_parser = PageParser(targeted_folder=html_test_folder)
	suppliers = page_parser.detected_suppliers()
	products = page_parser.detected_products()
	assert len(suppliers) == 113
	assert len(products) == 137
