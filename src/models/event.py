from sqlalchemy import Column, Integer, String, DateTime

from src.database.postgres import Base


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    data = Column(String)
    event_type = Column(String)
    timestamp = Column(DateTime)


