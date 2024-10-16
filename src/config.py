import configparser
import sys
import os
import os.path

class Config:
    def __init__(self, config_file_path: str):
        self._config_data = configparser.ConfigParser()
        self._config_data.read(config_file_path)

    def openai_api_key(self):
        env_value = os.environ.get("POKORABI_OPENAI_API_KEY")
        if env_value is not None:
            return env_value
        value = self._config_data.get("openai", "api_key", fallback="")
        return value

    def use_internal_website(self):
        env_value = os.environ.get("POKORABI_ENABLE_BUILTIN_WEBSITE")
        if env_value is not None:
            return env_value
        value = self._config_data.get("website", "enable_website", fallback="no")
        if value == "yes":
            return True
        return False

    def website_template_path(self):
        env_value = os.environ.get("POKORABI_WEBSITE_TEMPLATE_PATH")
        if env_value is not None:
            return env_value
        value = self._config_data.get("website", "template_path", fallback=os.path.join(sys.path[0], "templates"))
        return value

app_config = None

def initialize_app_config(config_file_path="./config.ini"):
    global app_config
    app_config = Config(config_file_path)
