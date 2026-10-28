from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    APP_NAME: str

    DEBUG: bool

    HOST: str

    PORT: int

    QDRANT_HOST: str
    QDRANT_PORT: int

    REDIS_HOST: str
    REDIS_PORT: int

    GEMINI_API_KEY: str

    class Config:
        env_file = ".env"


settings = Settings()