from typing import Dict, List
from pydantic import BaseSettings

class Settings(BaseSettings):
    DEBUG: bool = True
    
    PROJECT_NAME:str = "Newbie's Backend"
    API_V1_STR: str = "/api/v1"
    TAGS_METADATA: List[Dict[str, str]] = []

    HOST: str = '0.0.0.0'
    PORT: int = 8898

    class Config:
        env_prefix = 'NEWBIE_'


settings = Settings()