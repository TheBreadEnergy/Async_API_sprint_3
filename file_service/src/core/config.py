import os.path
from logging import config as logging_config

from pydantic import Field, PostgresDsn, RedisDsn
from pydantic_settings import BaseSettings, SettingsConfigDict
from src.core.logger import LOGGING


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="", env_file=".env")
    project_name: str = Field(
        "API для загрузки и хранения файлов", alias="PROJECT_NAME", env="PROJECT_NAME"
    )
    description: str = Field(
        "Загрузка, хранение и выдача информации и файлов,"
        " хранимых в файловом хранилище",
        alias="DESCRIPTION",
        env="DESCRIPTION",
    )
    version: str = Field("1.0.0", alias="VERSION", env="VERSION")
    redis_conn: RedisDsn = Field(..., alias="REDIS_CONN", env="REDIS_CONN")
    base_dir: str = os.path.dirname(os.path.abspath(__file__))
    postgres_conn: PostgresDsn = Field(..., alias="POSTGRES_CONN", env="POSTGRES_CONN")
    s3_bucket: str = Field(..., alias="S3_BUCKET", env="S3_BUCKET")


settings = Settings()


logging_config.dictConfig(LOGGING)
