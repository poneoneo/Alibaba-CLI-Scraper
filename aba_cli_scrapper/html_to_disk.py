from pathlib import Path

import selectolax
from loguru import logger


def _create_folder(folder_name: str):
    logger.info(f"Create folder with {folder_name} as name if not exists yet ...")
    Path(folder_name).mkdir(exist_ok=True)
    return Path(folder_name)


def scripts_hunter(css_selector: str, parser_instance: selectolax.parser.HTMLParser):
    div_with_class_container_or_id_root = parser_instance.css_first(css_selector)
    if div_with_class_container_or_id_root is None:
        logger.warning(
            "Something went wrong with the parsing, an empty none value has been returned "
        )
        return None
    list_scripts = div_with_class_container_or_id_root.css("script")
    # print(list_scripts)
    json_result = ""
    for script in list_scripts:
        script_content = script.text()
        # print(script_content)
        if "window.__page__data =" in script_content:
            # print(script_content)
            json_result = (
                script.text()
                .replace("window.__page__data__config =", "")
                .replace("window.__page__data = window.__page__data__config.props", "")
                .replace("window.__page__data =", "")
                .strip("\n \t \b ")
            )
            break
    return json_result


def json_parser_to_dict(html_content: str | bytes, css_selector: str = ""):
    """Parse the HTML content of the page to get the divs with class `.organic-list.viewtype-list`

    :param html_content: The HTML content of the page
    :type html_content: str
    :return: A list of divs with class `.organic-list.viewtype-list`
    :rtype: list
    """

    # dont parse anything at this stage as we are going to parse later
    # print(html_content)
    body_parser = selectolax.parser.HTMLParser(html_content)
    # div_with_class_container_or_id_root = body_parser.css_first(css_selector)
    json_result = scripts_hunter(css_selector, body_parser)
    if json_result == "":
        json_result = scripts_hunter("div[id='root']", body_parser)
        # print(json_result)
        return json_result
    if json_result is None:
        return None
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
