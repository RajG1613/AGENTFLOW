from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "AgentFlow"
    APP_VERSION: str = "0.1.0"

    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000

    DATABASE_URL: str = (
        "postgresql+psycopg://agentflow:agentflow@localhost:5432/agentflow"
    )

    REDIS_URL: str = "redis://localhost:6379/0"

    JWT_SECRET: str = "CHANGE_ME"

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
    )


settings = Settings()