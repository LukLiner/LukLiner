from pydantic import BaseModel
from pydantic_settings import BaseSettings

class RunConfig(BaseModel):
    host:str = "0.0.0.0"
    port: str = 8000

class ApiPrefix(BaseModel):
    api_prefix: str = "/api"

class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    prefix: ApiPrefix = ApiPrefix()


settings = Settings()