import os

import dotenv
from pydantic import BaseSettings


class Config(BaseSettings):
    DEBUG: bool = False
    
    PG_HOST: str
    PG_PORT: int
    PG_USER: str
    PG_PASSWORD: str
    PG_DATABASE: str

    class Config:
        env_file = os.path.join(os.path.dirname(__file__), '.env')
        dotenv.load_dotenv(env_file)


app_config = Config()
