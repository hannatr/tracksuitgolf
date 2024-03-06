import configparser
import logging
import logging.config
import os
import pathlib
from logging import Logger

APP_NAME = "tsg_api"

# Overwritten from config file!!!
# Do not import these variables directly (e.g., from config import DB_URL) to prevent race condition at startup!
# Supabase section
SUPABASE_URL = ""
SUPABASE_KEY = ""

# Logging section
LOG_LEVEL = logging.INFO
LOG_MAX_BYTES = 100
LOG_BACKUP_COUNT = 2
# End overwritten from config file

# Non-config file configuration
DATA_DIRECTORY = pathlib.Path(__file__).resolve().parent.parent.joinpath("data").resolve()
CONFIG_FILE = DATA_DIRECTORY.joinpath("config.ini").resolve()
LOG_FILE = DATA_DIRECTORY.joinpath(f"{APP_NAME}.log").resolve()
LOG_CONFIG = {}


def create_logger():
    global APP_NAME, LOG_LEVEL, LOG_MAX_BYTES, LOG_BACKUP_COUNT, LOG_FILE, LOG_CONFIG

    LOG_CONFIG = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                "()": "logging.Formatter",
                "fmt": "%(asctime)s %(levelname)-8s: [%(name)s] %(message)s",
            },
            "color": {
                "()": "uvicorn.logging.ColourizedFormatter",
                "fmt": "{asctime} {levelprefix:<8} [{name}] {message}",
                "style": "{",
                "use_colors": True,
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": LOG_LEVEL,
                "formatter": "color",
                "stream": "ext://sys.stdout",
            },
            "file": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": LOG_LEVEL,
                "formatter": "default",
                "filename": LOG_FILE,
                "maxBytes": LOG_MAX_BYTES,
                "backupCount": LOG_BACKUP_COUNT,
            },
        },
        "loggers": {
            APP_NAME: {
                "level": LOG_LEVEL,
                "handlers": ["console", "file"],
                "propagate": False,
            },
            "httpx": {
                "level": LOG_LEVEL,
                "handlers": ["console", "file"],
                "propagate": False,
            },
        },
    }

    logging.config.dictConfig(LOG_CONFIG)


def load_config_file() -> None:
    """Load config file and overwrite default values."""
    global CONFIG_FILE, SUPABASE_URL, SUPABASE_KEY, LOG_LEVEL, LOG_MAX_BYTES, LOG_BACKUP_COUNT
    config = configparser.ConfigParser()

    try:
        if not CONFIG_FILE.exists():
            raise configparser.Error("Could not find config file")

        config.read(CONFIG_FILE)
        SUPABASE_URL = config["supabase"]["url"]
        SUPABASE_KEY = os.getenv("SUPABASE_KEY")

        LOG_LEVEL = config["logging"]["log_level"]
        LOG_MAX_BYTES = int(config["logging"]["max_bytes"])
        LOG_BACKUP_COUNT = int(config["logging"]["backup_count"])
    except (configparser.Error, KeyError, ValueError) as e:
        print(f"Error reading config file {CONFIG_FILE}:")
        raise e


def get_logger(suffix: str = None) -> Logger:
    """Get the logger for the application."""
    global APP_NAME
    return logging.getLogger(APP_NAME + (f".{suffix}" if suffix else ""))


def load_configuration() -> Logger:
    """Run the configuration logic and return the application logger."""
    load_config_file()
    create_logger()
    return get_logger()
