from asyncio import Task
import html
from pathlib import Path
import json 

import selectolax
from loguru import logger


def _create_folder(folder_name: str):
    logger.info(f"Create folder with {folder_name} as name if not exists yet ...")
    Path(f"{folder_name}").mkdir(exist_ok=True)
    return Path(f"{folder_name}")


def json_parser_to_dict(html_content: str | bytes,css_selector: str = ""):
    """Parse the HTML content of the page to get the divs with class `.organic-list.viewtype-list`

    :param html_content: The HTML content of the page
    :type html_content: str
    :return: A list of divs with class `.organic-list.viewtype-list`
    :rtype: list
    """

    # dont parse anything at this stage as we are going to parse later
    # print(html_content)
    body_parser = selectolax.parser.HTMLParser(html_content)
    script_div = body_parser.css_first(css_selector)
    if script_div is None:
        logger.warning(
            "any HTML content  match the selector 'body > div.container > script:nth-child(9)', None will be returned and you may not have enough data as expected"
        )
        return None
    json_result = script_div.text().replace("window.__page__data__config =","").replace("window.__page__data = window.__page__data__config.props","").strip("\n \t \b ")
    if json_result is None:
        logger.warning(
            "any HTML content  match the selector '.organic-list', None value has been returned"
        )
        raise ValueError("None value has been returned")
    
    elif "window.__icbusearch_layout_i18n_kv__" in json_result:
        json_result = json_parser_to_dict(html_content=html_content, css_selector="body > div.container > script:nth-child(9)")
        return json_result
    else:
        # print(json_result)
        return json_result.strip()


@logger.catch()
def write_to_disk(folder_name: str, pages_contents: list[str]):
    """
    Writes list's contents HTML pages to disk.

    Args:
        folder_name (str): The name of the folder where the HTML files will be saved.
        pages_contents (list[str]): A list of strings representing the contents of the HTML pages.

    Returns:
        None

    Raises:
        None

    Side Effects:
        - Creates a folder with the given name if it does not exist.
        - Saves each HTML page as a separate file in the folder.
        - Logs the progress of saving each HTML page.

    Example Usage:
        write_to_disk("my_folder", ["<html>...</html>", "<html>...</html>"])
    """

    logger.info("Saving your scrapping result in disk...")
    path_obj = _create_folder(folder_name)
    for page_number, content in enumerate(pages_contents):
        # parsed_content = json_parser_to_dict(html_content=content, css_selector="body > div.container > script:nth-child(8)")
        # # print(parsed_content)
        # if parsed_content is None:
        #     logger.warning(
        #         f"parsed content is none"
        #     )
        #     continue
        # json_as_dict = json.loads(parsed_content)
        # print(json_as_dict)
        # print(type(json_as_dict))
        # json_as_str = json.dumps(json_as_dict, indent=4)
        with open(
            (path_obj / f"page_{page_number+1}.html").resolve(), "w", encoding="utf-8"
        ) as file:
            file.write(content)
        logger.info(
            f"Html content from page {page_number+1} has been saved succesfully !"
        )


if __name__ == "__name__":
    ...
