import pytest
from aba_cli_scrapper.scrape_from_disk import PageParser

@pytest.mark.filterwarnings("ignore::pytest.PytestUnraisableExceptionWarning")
@pytest.mark.filterwarnings("ignore:: RuntimeWarning")
def test_count_suppliers_and_products():
	page_parser = PageParser(targeted_folder="./Air_fryers")
	suppliers = page_parser.detected_suppliers()
	products = page_parser.detected_products()
	assert len(suppliers) == 46
	assert len(products) == 48
