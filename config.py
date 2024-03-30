import datetime

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    print(f'starting Settings at {datetime.datetime.utcnow()}')
    app_name: str = "Awesome API"
    admin_email: str
    items_per_user: int = 50
    model_config = SettingsConfigDict(env_file=".env")

    # def __init__(self):
    #     super()
    #     print(f'starting Settings at {datetime.datetime.utcnow()}')



