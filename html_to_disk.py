from pathlib import Path
from loguru import logger
import sys


logger.add(sys.stderr,colorize=True)

def _create_folder(folder_name:str):
    logger.info(f"Create folder with {folder_name} as name if not exists")
    Path(f"{folder_name}").mkdir(exist_ok=True)
    return Path(f"{folder_name}")

@logger.catch()
def write_to_disk(folder_name:str, pages_contents: list[str]):
    logger.info("Saving your scrapping result in disk...")
    path_obj = _create_folder(folder_name)
    for page_number,content in enumerate(pages_contents):
            with open((path_obj/f"page_{page_number+1}.html").resolve() ,'a+',encoding='utf-8') as file:
                    file.write(content)
            logger.info(f"Html content from page {page_number+1} has been saved succesfully !")
            

if __name__ =="__name__":...
