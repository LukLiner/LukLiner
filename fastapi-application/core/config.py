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
    naming_convection :dict[str,str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s"
    }


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