from tortoise import Tortoise, connections

from config.config import app_config


DB_CONFIG = {
    'connections': {
        'default': {
            'engine': 'tortoise.backends.asyncpg',
            'credentials': {
                'host': app_config.PG_HOST,
                'port': app_config.PG_PORT,
                'user': app_config.PG_USER,
                'password': app_config.PG_PASSWORD,
                'database': app_config.PG_DATABASE,
            },
        }
    },
    'apps': {
        'models': {
            'models': ['database.models'],
            'default_connection': 'default'
        }
    }
}


class Database:
    _config: dict

    def __init__(self, config: dict):
        self._config = config

    async def connect(self) -> None:
        await Tortoise.init(config=self._config)

    @staticmethod
    async def disconnect() -> None:
        await connections.close_all()


def get_database() -> Database:
    return Database(config=DB_CONFIG)
