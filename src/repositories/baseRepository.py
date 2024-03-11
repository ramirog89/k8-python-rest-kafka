from fastapi import Depends
from typing import Any

from src.database.setup import get_postgres_db, get_mongo_db


class BaseRepository:
    postgres_session: Any = None
    mongo_session: Any = None

    def __init__(
            self,
            postgres_session: get_postgres_db = Depends(),
            mongo_session: get_mongo_db = Depends()
        ):
        self.postgres_session = postgres_session
        self.mongo_session = mongo_session
