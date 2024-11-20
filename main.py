from asyncio import Event

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from config.sqlite_config import Base, engine, get_db
from controller import router
from models.product import Product

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

@app.get("/sqlite/products/")
def read_products_sqlite(db: Session = Depends(get_db)):
    products = db.query(Product).all()
    return products
