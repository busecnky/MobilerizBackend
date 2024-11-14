from sqlalchemy.orm import Session

from models.vendor import Vendor


def create_vendor(db: Session, VendorData):
    vendor = Vendor(**VendorData)
    db.add(vendor)
    db.commit()
    db.refresh(vendor)
    return vendor

def get_all_vendors(db: Session):
    return db.query(Vendor).all()

def get_vendor_by_id(db: Session, vendor_id: int):
    return db.query(Vendor).filter(Vendor.id == vendor_id).first()