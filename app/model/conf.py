from typing import Optional
from pydantic import BaseModel


class TwitchLogin(BaseModel):
    username: str
    password: str
    cookies: dict
    two_factor: Optional[str]


class ConfigModel(BaseModel):
    twitch: TwitchLogin
