from urllib.parse import urlparse

from dotenv import load_dotenv
from pydantic import Field, PostgresDsn
from pydantic_settings import BaseSettings

DEFAULT_POSTGRES_URL: str = "postgresql+psycopg://user:password@localhost:5432/dbname"

load_dotenv()


class DBConfig(BaseSettings):
    app_name: str = "foobar-db"
    database_url: PostgresDsn = Field(default=PostgresDsn(DEFAULT_POSTGRES_URL))

    @property
    def db_url(self) -> str:
        return self.database_url.encoded_string()

    @property
    def scheme(self) -> str:
        return self.database_url.scheme

    @property
    def host(self) -> str | None:
        return urlparse(self.db_url).hostname

    @property
    def user(self) -> str | None:
        return urlparse(self.db_url).username

    @property
    def password(self) -> str | None:
        return urlparse(self.db_url).password

    @property
    def port(self) -> int | None:
        return urlparse(self.db_url).port


class ApiConfig(BaseSettings):
    """Settings for the FastAPI server."""

    app_name: str = "Foobar"
    host: str = "localhost"
    port: int = 8000
    environment: str = "development"

    @property
    def reload(self) -> bool:
        return self.environment == "development"


db_config = DBConfig()
api_config = ApiConfig()
