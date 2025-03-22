from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    LOG_LEVEL: str
    
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASS: str
    SECRET_KEY: str
    ALGORITHM: str

    class Config:
        env_file = ".env"

settings = Settings()