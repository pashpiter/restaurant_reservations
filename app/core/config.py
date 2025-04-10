from pydantic import Field
from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    debug: bool = Field('True', alias='DEBUG')


class PostgresSettings(BaseSettings):
    host: str = Field('localhost', alias='POSTGRES_HOST')
    port: int = Field(5432, alias='POSTGRES_PORT')
    user: str = Field('postgres', alias='POSTGRES_USER')
    password: str = Field('postgres', alias='POSTGRES_PASSWORD')
    db_name: str = Field('postgres', alias='POSTGRES_DB')

    @property
    def postgres_url(self) -> str:
        return 'postgresql+asyncpg://{}:{}@{}:{}/{}'.format(
            self.user,
            self.password,
            self.host,
            self.port,
            self.db_name
        )


class Settings:
    app: AppSettings = AppSettings()
    postgres: PostgresSettings = PostgresSettings()


settings = Settings()
