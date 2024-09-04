from pathlib import Path

import selectolax
from loguru import logger


def _create_folder(folder_name: str):
	"""Create a folder with the name `folder_name` if it doesn't exist yet

	:param folder_name:
	:type folder_name: str
	:return: Path
	:rtype: Path object
	"""
	logger.info(f"Create folder with {folder_name} as name if not exists yet ...")
	Path(folder_name).mkdir(exist_ok=True)
	return Path(folder_name)


def scripts_hunter(css_selector: str, parser_instance: selectolax.parser.HTMLParser):
	if css_selector != "":
		div_with_id_root = parser_instance.css_first(css_selector)
		if div_with_id_root is None:
			logger.warning(
				"Something went wrong with the parsing, an empty none value has been returned "
			)
			return None
		else:
			list_scripts = div_with_id_root.css("script")
	else:
		list_scripts = parser_instance.css("script")
	json_result = ""
	for script in list_scripts:
		script_content = script.text()
		# print(script_content)
		if "window.__page__data =" in script_content:
			# print(script_content)
			json_result = (
				script.text()
				.replace("window.__page__data__config =", "")
				.replace(
					"window.__page__data = window.__page__data__config.props",
					"",
				)
				.replace("window.__page__data =", "")
				.strip("\n \t \b ")
			)
			break
	return json_result


def json_hunter(html_content: str | bytes, css_selector: str = ""):
	"""Parse the HTML content of the page to get all json content in the divs where eitheir class=`.organic-list.viewtype-list` or  id='root'.

	:param html_content: The HTML content of the page
	:type html_content: str
	:return: A list of divs with class `.organic-list.viewtype-list`
	:rtype: list
	"""
	body_parser = selectolax.parser.HTMLParser(html_content)
	json_result = scripts_hunter(css_selector, body_parser)
	if json_result is None:
		json_result = scripts_hunter("", body_parser)
		return json_result
	return json_result.strip()


@logger.catch()
def write_to_disk(folder_name: str, pages_contents: list[str]):
	"""Save the content of each page as a separate HTML file in a folder named `folder_name`.

	:param folder_name: The name of the folder where the HTML pages will be saved
	:type folder_name: str
	:param pages_contents: A list of strings containing the HTML content of each page
	:type pages_contents: list[str]
	:return: None
	"""
	logger.info("Saving your scrapping result in disk...")
	path_obj = _create_folder(folder_name)
	for page_number, content in enumerate(pages_contents):
		with open(
			(path_obj / f"page_{page_number + 1}.html").resolve(),
			"w",
			encoding="utf-8",
		) as file:
			file.write(content)
		logger.info(f"Html content from page {page_number + 1} has been saved succesfully !")


if __name__ == "__name__":
	...
