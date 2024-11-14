import httpx
from sqlalchemy.orm import Session

from repositories.product_repository import create_product
from repositories.vendor_repository import create_vendor


async def create_vendor_and_fetch_products(db: Session, vendor_data: dict):
    vendor = create_vendor(db, vendor_data)

    async with httpx.AsyncClient() as client:
        response = await client.get(vendor.base_url)
        if response.status_code == 200:
            products_data = response.json()
            products = []
            for product in products_data:
                create_product(db, product, vendor_id=vendor.id)
                products.append(product)

            return vendor, products
        else:
            print(f"Failed to fetch data from {vendor.vendor_name}: {response.status_code}")
