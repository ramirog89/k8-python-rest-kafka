from src import models
from src.database.postgres import engine, SessionLocal
from src.database.mongo import mongodb_client

models.Base.metadata.create_all(bind=engine)

def get_postgres_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_mongo_db():
    try:
        db =  mongodb_client
        return db
    except Exception as error:
        raise error

