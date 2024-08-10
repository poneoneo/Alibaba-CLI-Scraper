import os

from dotenv import load_dotenv

load_dotenv(override=True)
SBR_WS_CDP_LIST: str  = os.environ.get("SBR_WS_CDP_LIST", "")
LOGURU_LEVEL: str | None = os.environ.get("LOGURU_LEVEL")
