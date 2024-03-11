from typing import List
from fastapi import Depends

from src.repositories import EventRepository
from src.models.event import Event
from src.schemas.event import EventCreate, EventRecord


class EventService:

    def __init__(
        self,
        eventRepository: EventRepository = Depends(),
    ):
        self.eventRepository = eventRepository

    def getPostgresEventList(self) -> List[Event]:
        return self.eventRepository.getPostgresEventList()

    def createPostgresEvent(self, event: EventCreate) -> Event:
        try:
            return self.eventRepository.createPostgresEvent(event)
        except Exception as err:
            raise Exception(err)

    def getMongoEventList(self) -> List[EventRecord]:
        return self.eventRepository.getMongoEventList()

    def createEventRecord(self, event: EventCreate) -> EventRecord:
        return self.eventRepository.createEventRecord(event)