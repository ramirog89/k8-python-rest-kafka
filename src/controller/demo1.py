from fastapi import APIRouter, Depends, HTTPException

from src.service.event import EventService
from src.schemas.event import EventCreate


router = APIRouter()


@router.get('/demo1', tags=['demo1'])
async def get_events(service: EventService = Depends()):
    try:
        return service.getPostgresEventList()
    except Exception as error:
        raise HTTPException(status_code=400, detail=str(error))


@router.post("/demo1", tags=['demo1'])
async def create_event(event: EventCreate, service: EventService = Depends()):
    try:
        return service.createPostgresEvent(event)
    except Exception as error:
        raise HTTPException(status_code=400, detail=str(error))
