import asyncio
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.sqlite_config import get_db
from models.product import Product
from repositories.vendor_repository import create_vendor
from services.kafka_consumer import consume_messages_from_kafka
from services.vendor_service import fetch_product_from_vendor_by_name

router = APIRouter()


@router.post("/create_vendor")
async def create_vendors(vendor_data: dict, db: Session = Depends(get_db)):
    return create_vendor(db, vendor_data)


@router.get("/products")
def find_all_products(db: Session = Depends(get_db)):
    return db.query(Product).all()


@router.get("/products/{product_name}")
async def get_product_from_sqlite_or_vendor(product_name: str, db: Session = Depends(get_db)):
    products = db.query(Product).filter(Product.product_name == product_name).all()

    if not products:
        await fetch_product_from_vendor_by_name(product_name)

        consume_messages_from_kafka(db, product_name)

        await asyncio.sleep(1)
        products = db.query(Product).filter(Product.product_name == product_name).all()

        if not products:
            raise HTTPException(status_code=404, detail="Product not found in vendors")

    product_list = [
        {
            "product_name": product.product_name,
            "price": product.price,
            "description": product.description,
            "image_url": product.image_url,
            "vendor_id": product.vendor_id,
        }
        for product in products
    ]

    return {"status": "success", "products": product_list}
