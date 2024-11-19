import asyncio
from asyncio import Event
from contextlib import asynccontextmanager

from fastapi import FastAPI
from config.sqlite_config import Base, engine
from controller import router
from services.kafka_consumer import consume_messages_from_kafka

app = FastAPI(debug=True)

Base.metadata.create_all(bind=engine)
app.include_router(router.router)
shutdown_event = Event()

@app.get("/")
async def root():
    return {"message": "Unified Vendor Data API"}
