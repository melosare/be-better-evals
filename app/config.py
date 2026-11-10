from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "be-better-evals"
    app_env: str = "development"
    debug: bool = True

    database_url: str = "sqlite:///./be_better_evals.db"

    openai_api_key: str | None = None
    openai_model: str = "gpt-4.1-mini"

    smtp_host: str | None = None
    smtp_port: int = 587
    smtp_username: str | None = None
    smtp_password: str | None = None

    alert_email_from: str | None = None
    alert_email_to: str | None = None

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
