from typing import Any
from pydantic import BaseModel

class EventBase(BaseModel):
    data: Any
    event_type: str

    class Config:
        from_attributes = True

class EventCreate(EventBase):
    pass

class Event(EventBase):
    id: int
    timestamp: Any

class EventRecord(EventBase):
    id: str
    timestamp: Any

