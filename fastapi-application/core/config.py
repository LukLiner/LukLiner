from pydantic import BaseModel, MySQLDsn, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict

class RunConfig(BaseModel):
    host:str = "127.0.0.1"
    port: str = 8000

class ApiPrefix(BaseModel):
    api_prefix: str = "/api"

class DataBaseSettings(BaseModel):
    url:str
    echo: bool = True
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_nested_delimiter="__",
        case_sensitive=False,
        env_prefix="APP_CONFIG_",
    )
    run: RunConfig = RunConfig()
    prefix: ApiPrefix = ApiPrefix()
    db: DataBaseSettings = DataBaseSettings(url="mysql+asyncmy://bestuser:bestuser@127.0.0.1:3306/shop")


settings = Settings()