from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    logging_level: str = 'DEBUG'
    api_base_url: str | None = None


settings = Settings()


LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            '()': 'python3_commons.logging.formatter.JSONFormatter',
        },
    },
    'filters': {
        'info_and_below': {
            '()': 'python3_commons.logging.filters.filter_maker',
            'level': 'INFO'
        }
    },
    'handlers': {
        'default_stdout': {
            'level': settings.logging_level,
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
            'formatter': 'default',
            'filters': ['info_and_below', ],
        },
        'default_stderr': {
            'level': 'WARNING',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stderr',
            'formatter': 'default',
        },
    },
    'loggers': {
        '': {
            'handlers': ['default_stderr', 'default_stdout', ],
        },
        'interview': {
            'handlers': ['default_stderr', 'default_stdout', ],
            'level': settings.logging_level,
            'propagate': False,
        },
        '__main__': {
            'handlers': ['default_stderr', 'default_stdout', ],
            'level': settings.logging_level,
            'propagate': False,
        }
    }
}
