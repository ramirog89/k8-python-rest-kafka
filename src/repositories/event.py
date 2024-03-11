from typing import List, Any
from datetime import datetime, timezone

from src.repositories import BaseRepository
from src.schemas import event as schema
from src.models import event as model


class EventRepository(BaseRepository):

    def getPostgresEventList(self) -> List[model.Event]:
        query = self.postgres_session.query(model.Event)
        return query.all()

    def createPostgresEvent(self, event: schema.EventCreate) -> model.Event:
        db_event = model.Event(
            data=event.data,
            event_type=event.event_type,
            timestamp=datetime.now(tz=timezone.utc)
        )
        self.postgres_session.add(db_event)
        self.postgres_session.commit()
        self.postgres_session.refresh(db_event)
        return db_event
    

    def getMongoEventList(self):
        event_collection = self.mongo_session.db.event_collection
        result = []
        for record in event_collection.find():
            result.append({
                'id': str(record['_id']),
                'data': record['data'],
                'event_type': record['event_type'],
                'timestamp': record['timestamp'] if 'timestamp' in record else None,
            })
        return result

    def createEventRecord(self, event: schema.EventCreate) -> Any:
        event_collection = self.mongo_session.db.event_collection
        payload = { **dict(event), 'timestamp': datetime.now(tz=timezone.utc) }
        record = event_collection.insert_one(payload)
        result = event_collection.find_one({"_id": record.inserted_id })
        return {
            'id': str(result['_id']),
            'data': result['data'],
            'event_type': result['event_type'],
            'timestamp': result['timestamp']
        }
