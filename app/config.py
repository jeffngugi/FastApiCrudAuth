import os
import secrets
from typing import List, Optional, Union

from pydantic import AnyHttpUrl, PostgresDsn, field_validator
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = os.environ.get("SECRET_KEY", secrets.token_urlsafe(32))
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 8 days
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @field_validator("BACKEND_CORS_ORIGINS", mode='before')
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    PROJECT_NAME: str = "FastAPI CRUD App"
    
    # Database Configuration
    POSTGRES_SERVER: str = os.environ.get("PGHOST", "localhost")
    POSTGRES_USER: str = os.environ.get("PGUSER", "postgres")
    POSTGRES_PASSWORD: str = os.environ.get("PGPASSWORD", "postgres")
    POSTGRES_DB: str = os.environ.get("PGDATABASE", "app")
    POSTGRES_PORT: str = os.environ.get("PGPORT", "5432")
    DATABASE_URL: Optional[PostgresDsn] = os.environ.get(
        "DATABASE_URL", 
        f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
    )

    class Config:
        case_sensitive = True

settings = Settings()
