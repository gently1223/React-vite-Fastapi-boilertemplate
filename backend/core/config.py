import os

from pydantic import BaseSettings

current_dir = os.path.dirname(os.path.abspath(__file__))
db_file_path = os.path.join(current_dir, "assessment.db")

class Config(BaseSettings):
    ENV: str = "development"
    DEBUG: bool = True
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8001
    WRITER_DB_URL: str = "sqlite+aiosqlite:///assessment.db"
    READER_DB_URL: str = "sqlite+aiosqlite:///assessment.db"
    JWT_SECRET_KEY: str = "easyric"
    JWT_ALGORITHM: str = "HS256"
    SENTRY_SDN: str = None
    CELERY_BROKER_URL: str = None
    CELERY_BACKEND_URL: str = None
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379


class DevelopmentConfig(Config):
    WRITER_DB_URL: str = "sqlite+aiosqlite:///assessment.db"
    READER_DB_URL: str = "sqlite+aiosqlite:///assessment.db"
    REDIS_HOST: str = "redis"
    REDIS_PORT: int = 6379


class LocalConfig(Config):
    WRITER_DB_URL: str = "sqlite+aiosqlite:///assessment.db"
    READER_DB_URL: str = "sqlite+aiosqlite:///assessment.db"


class ProductionConfig(Config):
    DEBUG: str = False
    WRITER_DB_URL: str = "sqlite+aiosqlite:///assessment.db"
    READER_DB_URL: str = "sqlite+aiosqlite:///assessment.db"


def get_config():
    env = os.getenv("ENV", "local")
    config_type = {
        "dev": DevelopmentConfig(),
        "local": LocalConfig(),
        "prod": ProductionConfig(),
    }
    return config_type["prod"]


config: Config = get_config()
