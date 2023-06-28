import os

from pydantic import BaseSettings
from dotenv import load_dotenv

load_dotenv()

current_dir = os.path.dirname(os.path.abspath(__file__))
db_file_path = os.path.join(current_dir, os.getenv("DB_FILE_PATH"))

class Config(BaseSettings):
    ENV: str = "development"
    DEBUG: bool = os.getenv("DEBUG")
    APP_HOST: str = os.getenv("APP_HOST")
    APP_PORT: int = os.getenv("APP_PORT")
    WRITER_DB_URL: str = os.getenv("WRITER_DB_URL")
    READER_DB_URL: str = os.getenv("READER_DB_URL")
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY")
    JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM")
    SENTRY_SDN: str = os.getenv("SENTRY_SDN")
    CELERY_BROKER_URL: str = os.getenv("CELERY_BROKER_URL")
    CELERY_BACKEND_URL: str = os.getenv("CELERY_BACKEND_URL")


class DevelopmentConfig(Config):
    WRITER_DB_URL: str = os.getenv("WRITER_DB_URL")
    READER_DB_URL: str = os.getenv("READER_DB_URL")


class LocalConfig(Config):
    WRITER_DB_URL: str = os.getenv("WRITER_DB_URL")
    READER_DB_URL: str = os.getenv("READER_DB_URL")


class ProductionConfig(Config):
    DEBUG: str = False
    WRITER_DB_URL: str = os.getenv("WRITER_DB_URL")
    READER_DB_URL: str = os.getenv("READER_DB_URL")


def get_config():
    env = os.getenv("ENV", "local")
    config_type = {
        "dev": DevelopmentConfig(),
        "local": LocalConfig(),
        "prod": ProductionConfig(),
    }
    return config_type["prod"]


config: Config = get_config()
