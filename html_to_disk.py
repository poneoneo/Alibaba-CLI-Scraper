from pathlib import Path
from loguru import logger
import sys


logger.add(sys.stderr,colorize=True)

def _create_folder(folder_name:str):
    logger.info(f"Create folder with {folder_name} as name if not exists")
    Path(f"{folder_name}").mkdir(exist_ok=True)
    return Path(f"{folder_name}")

# def _create_file(current_folder:Path,file_name:str):
#     (current_folder/f"{file_name}").touch()

def write_to_disk(folder_name:str, html_contents: list[str]):
    logger.info("Saving your scrapping result in disk...")
    path_obj = _create_folder(folder_name)
    for page_number,html_content in enumerate(html_contents,start=1):
        # _create_file(path_obj,f"page_{page_number}.html")
        with open((path_obj/f"page_{page_number}.html").resolve() ,"w",encoding='utf-8') as file:
            file.write(html_content)
        logger.info(f"Html content from page {page_number} has been saved succesfully !")

if __name__ =="__name__":...
