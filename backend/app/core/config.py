
# * define env variables-loaders

from rich import print
from app.core.logger import logger
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """ App Settings & variable environments """
    # ==>DB<==
    DB_PASSWORD: str
    DB_USERNAME: str
    DB_HOSTNAME: str
    DB_PORT: str
    DB_NAME: str
    ENVIRONMENT: str

    class Config: #*=> to set env vars source
        env_file = ".env"

try:
    # create an instance
    settings = Settings()
except Exception as exc:
    print("[red][!]Unable To Reach `.env` file ![red]")
    logger.error(f"Failed To Reach `.env` file with reason:{exc}")


# allowed requests origins 
allowed_origins = [
    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:5175",
]

logger.success("<>")