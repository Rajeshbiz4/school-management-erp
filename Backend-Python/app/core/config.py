from functools import lru_cache
from typing import List

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "School ERP Backend API"
    app_env: str = "local"
    api_prefix: str = "/api/v1"
    cors_origins: str = "http://localhost:3000,http://localhost:5173,http://localhost:8081"

    use_in_memory_db: bool = True

    cosmos_endpoint: str = ""
    cosmos_key: str = ""
    cosmos_database_name: str = "school_erp_db"
    cosmos_employee_container: str = "employees"
    cosmos_maintenance_container: str = "maintenance_tickets"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    @property
    def cors_origin_list(self) -> List[str]:
        return [origin.strip() for origin in self.cors_origins.split(",") if origin.strip()]


@lru_cache
def get_settings() -> Settings:
    return Settings()
