import configparser
import sys
import os.path

class Config:
    def __init__(self, config_file_path: str):
        self._config_data = configparser.ConfigParser()
        self._config_data.read(config_file_path)

    def openai_api_key(self):
        value = self._config_data.get("openai", "api_key", fallback="")
        return value

    def use_internal_website(self):
        value = self._config_data.get("website", "enable_website", fallback="yes")
        if value == "yes":
            return True
        return False

    def website_template_path(self):
        value = self._config_data.get("website", "template_path", fallback=os.path.join(sys.path[0], "templates"))
        return value

app_config = None

def initialize_app_config(config_file_path="./config.ini"):
    global app_config
    app_config = Config(config_file_path)
