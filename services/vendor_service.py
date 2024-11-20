import httpx
from fastapi import HTTPException
from config.sqlite_config import get_db
from models.vendor import Vendor
from services.converter_service import convert_data_for_vendor
from services.kafka_producer import send_message_to_kafka


async def find_all_vendors():
    db = next(get_db())
    return db.query(Vendor).all()


async def fetch_product_from_vendor_by_name(product_name: str):
    vendors = await find_all_vendors()

    if vendors is None:
        raise HTTPException(status_code=404, detail="There is not any vendor to search")

    for vendor in vendors:
        async with httpx.AsyncClient() as client:
            response = await client.get(vendor.base_url)
            if response.status_code == 200:
                products = response.json()
                for product in products:
                    product_data = convert_data_for_vendor(product, vendor.vendor_name)
                    if product_data["product_name"].lower() == product_name.lower():
                        kafka_message = {
                            "product_name": product_data["product_name"],
                            "price": product_data["price"],
                            "description": product_data["description"],
                            "image_url": product_data["image_url"],
                            "vendor_id": vendor.id
                        }
                        send_message_to_kafka({"product": kafka_message})

                        return product, vendor.vendor_name

    return None, None