from asyncio import Event

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config.sqlite_config import Base, engine
from controller import router

app = FastAPI(debug=True)

origins = [
    "http://localhost",
    "http://localhost:60143",
    "http://127.0.0.1:8016",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)
app.include_router(router.router)
shutdown_event = Event()

@app.get("/")
async def root():
    return {"message": "Unified Vendor Data API"}
