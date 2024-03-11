from pymongo import MongoClient

from src.config.settings import mongodb_uri

mongodb_client = MongoClient(mongodb_uri)
