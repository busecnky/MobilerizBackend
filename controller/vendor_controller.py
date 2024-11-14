from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session

from config.sqlite_config import SessionLocal, Base
from services.vendor_service import create_vendor_and_fetch_products

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/vendors_and_products")
async def create_vendor_and_fetch_products_endpoint(vendor_data: dict, db: Session = Depends(get_db)):
    result = await create_vendor_and_fetch_products(db, vendor_data)
    return result