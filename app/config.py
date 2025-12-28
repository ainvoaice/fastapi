# app/config.py
from pydantic_settings import BaseSettings
from typing import List, Optional
from functools import lru_cache

class Settings(BaseSettings):
    # Database
    DATABASE_URL: str = "postgresql+asyncpg://postgres:password@localhost/invoicedb"
    DB_POOL_SIZE: int = 5
    DB_MAX_OVERFLOW: int = 10
    DB_ECHO: bool = False
    
    # Seed Data
    SEED_DATA: bool = True  # Whether to seed data on startup
    SEED_TYPE: str = "full"  # 'full', 'test', or 'none'
    SEED_SAMPLE_SIZE: int = 10  # Number of sample records to create
    
    # Application
    PROJECT_NAME: str = "Invoice Management API"
    VERSION: str = "1.0.0"
    DESCRIPTION: str = "Backend API for invoice management"
    ALLOWED_ORIGINS: List[str] = ["http://localhost:3000", "http://127.0.0.1:3000"]
    
    # Security
    SECRET_KEY: str = "your-secret-key-here-change-in-production"
    
    class Config:
        env_file = ".env"
        case_sensitive = True
        
@lru_cache()
def get_settings_singleton():
    return Settings()