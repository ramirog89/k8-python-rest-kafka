from logging import config

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.controller import demo1, demo2
from src.service.kafka.consumer import listen_kafka_messages
from src.config.logger import loggerConfig

# Setup logger
config.dictConfig(loggerConfig)

app = FastAPI()
app.debug = True
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(demo1.router)
app.include_router(demo2.router)
listen_kafka_messages()