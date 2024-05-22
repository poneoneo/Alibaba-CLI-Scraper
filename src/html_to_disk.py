

from pathlib import Path
from loguru import logger


def _create_folder(folder_name:str):
    logger.info(f"Create folder with {folder_name} as name if not exists yet ...")
    Path(f"{folder_name}").mkdir(exist_ok=True)
    return Path(f"{folder_name}")

@logger.catch()
def write_to_disk(folder_name:str, pages_contents: list[str]):
    """
    Writes the contents of a list of HTML pages to disk.

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
    for page_number,content in enumerate(pages_contents):
            with open((path_obj/f"page_{page_number+1}.html").resolve() ,'a+',encoding='utf-8') as file:
                    file.write(content)
            logger.info(f"Html content from page {page_number+1} has been saved succesfully !")
            

if __name__ =="__name__":...
