
import os
from dotenv import load_dotenv

REQUIRED_KEYS = [
    "TELEGRAM_BOT_TOKEN",
    "LOG_FILE_NAME",
    "DAILY_REPORT_FILENAME"
]

OPTIONAL_KEYS = {
    "ALLOWED_GROUP_ID": "",
    "ENABLE_LOGGING": "True",
    "DAILY_REPORT_ENABLED": "True",
    "MAX_RESULTS": "4",
    "DEFAULT_LANGUAGE": "he",
    "ENABLE_IMAGES": "True"
}

class BotConfig:
    def __init__(self, env_path=".env.full"):
        load_dotenv(dotenv_path=env_path)
        self.config = {}
        for key in REQUIRED_KEYS:
            value = os.getenv(key)
            if not value:
                raise ValueError(f"Missing required config key: {key}")
            self.config[key] = value
        for key, default in OPTIONAL_KEYS.items():
            self.config[key] = os.getenv(key, default)

    def get(self, key):
        return self.config.get(key)

    def __getitem__(self, key):
        return self.get(key)
