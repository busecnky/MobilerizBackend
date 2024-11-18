from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from config.sqlite_config import get_db
from models.product import Product
from services.kafka_producer import send_message_to_kafka
from services.vendor_service import create_vendor_and_fetch_products

router = APIRouter()


@router.post("/vendors_and_products")
async def create_vendor_and_fetch_products_endpoint(vendor_data: dict, db: Session = Depends(get_db)):
    result = await create_vendor_and_fetch_products(db, vendor_data)
    return result

@router.get("/products/{product_id}")
async def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    kafka_message = {
        "product_id": product.id,
        "name": product.product_name,
        "price": product.price,
        "description": product.description,
        "image_url": product.image_url,
    }
    send_message_to_kafka({"product": kafka_message})
    return {"status": "success", "message": kafka_message}
