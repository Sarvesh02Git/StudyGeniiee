# backend/utils/logger_config.py
import os
import logging.config

def setup_logging():
    """
    Sets up the logging configuration for the FastAPI application.
    """
    LOG_DIR = "logs"
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    LOGGING_CONFIG = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "standard": {
                "format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
                "datefmt": "%Y-%m-%d %H:%M:%S",
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "standard",
                "stream": "ext://sys.stderr",
            },
            "file": {
                "class": "logging.FileHandler",
                "formatter": "standard",
                "filename": os.path.join(LOG_DIR, "app.log"),
            },
        },
        "loggers": {
            "uvicorn": {"handlers": ["console"], "level": "INFO"},
            "uvicorn.error": {"level": "INFO"},
            "root": {"handlers": ["console", "file"], "level": "DEBUG"},
            "app": {"handlers": ["console", "file"], "level": "DEBUG", "propagate": False},
        },
    }
    logging.config.dictConfig(LOGGING_CONFIG)