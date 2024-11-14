import uvicorn
from fastapi import FastAPI
from config.sqlite_config import Base, engine
from controller import vendor_controller

app = FastAPI(debug=True)

Base.metadata.create_all(bind=engine)
app.include_router(vendor_controller.router)

@app.get("/")
async def root():
    return {"message": "Unified Vendor Data API"}
