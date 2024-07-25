# app/core/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    ENCRYPTION_KEY: str  
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    class Config:
        env_file = "env/.env"
        env_file_encoding = "utf-8"

settings = Settings()

