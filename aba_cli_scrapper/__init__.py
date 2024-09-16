import os

from .ascii import get_current_version

from dotenv import load_dotenv

__version__ = get_current_version()

load_dotenv(override=True)
BRIGHT_DATA_API_KEY: str = os.environ.get("BRIGHT_DATA_API_KEY", "")
SYPHOON_API_KEY: str = os.environ.get("SYPHOON_API_KEY", "")
LOGURU_LEVEL: str | None = os.environ.get("LOGURU_LEVEL")
