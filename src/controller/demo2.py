from fastapi import APIRouter, Depends, HTTPException
from typing import List

from src.service.event import EventService
from src.schemas.event import EventCreate, EventRecord


router = APIRouter()


@router.get('/demo2', tags=['demo2'], response_model=List[EventRecord])
async def get_events(service: EventService = Depends()):
    try:
        return service.getMongoEventList()
    except Exception as error:
        raise HTTPException(status_code=400, detail=str(error))


@router.post("/demo2", tags=['demo2'], response_model=EventRecord)
async def create_event(event: EventCreate, service: EventService = Depends()):
    try:
        return service.createEventRecord(event)
    except Exception as error:
        raise HTTPException(status_code=400, detail=str(error))
