import ujson
from app.model import ConfigModel


def load_config() -> ConfigModel:
    with open("config.json", "r", encoding="utf-8") as json_file:
        raw_dictionary: dict = ujson.load(json_file)
    return ConfigModel(**raw_dictionary)
