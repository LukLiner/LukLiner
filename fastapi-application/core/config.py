from pydantic import BaseModel, MySQLDsn
from pydantic_settings import BaseSettings

class RunConfig(BaseModel):
    host:str = "127.0.0.1"
    port: str = 8000

class ApiPrefix(BaseModel):
    api_prefix: str = "/api"

class DataBaseSettings(BaseModel):
    url:MySQLDsn
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10


class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    prefix: ApiPrefix = ApiPrefix()
    db: DataBaseSettings = DataBaseSettings


settings = Settings()