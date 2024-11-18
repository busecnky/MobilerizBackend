from fastapi import FastAPI
from config.sqlite_config import Base, engine
from controller import router

app = FastAPI(debug=True)

Base.metadata.create_all(bind=engine)
app.include_router(router.router)

@app.get("/")
async def root():
    return {"message": "Unified Vendor Data API"}
