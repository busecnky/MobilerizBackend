from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from config.sqlite_config import SessionLocal, Base
from models.vendor_data import VendorData
from services.vendor_service import fetch_vendors_and_save_db

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/vendors/fetch")
async def fetch_vendor_data(vendor_data: VendorData, db: Session = Depends(get_db)):
    vendor = db.query(VendorData).filter_by(vendor_name=vendor_data.vendor_name).first()

    if not vendor:
        raise HTTPException(status_code=404, detail="Item not found")

    await fetch_vendors_and_save_db(db, vendor_data)

    return {"status": "Data fetched and stored successfully"}