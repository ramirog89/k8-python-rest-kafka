loggerConfig = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "%(levelname)s:\t  %(message)s"
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "simple",
            "stream": "ext://sys.stdout"
        },
    },
    "loggers": {
        "debug": {
            "level": "DEBUG",
            "handlers": ["console"],
            "propagate": False
        },
    }
}