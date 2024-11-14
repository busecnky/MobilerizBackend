import httpx
from sqlalchemy.orm import Session

from repositories.product_repository import create_product
from repositories.vendor_repository import create_vendor
from services.converter_service import ConverterService


async def fetch_vendors_and_save_db(db: Session, VendorData):
    vendor = create_vendor(db, VendorData)

    async with httpx.AsyncClient() as client:
        response = await client.get(vendor.base_url)
        if response.status_code == 200:
            vendor_data = response.json()
            products = ConverterService.convert_to_product(vendor_data)
            for product in products:
                create_product(db, product, vendor_id=vendor.id)
        else:
            print(f"Failed to fetch data from {vendor.name}: {response.status_code}")
