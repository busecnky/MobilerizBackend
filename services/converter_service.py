from typing import Dict, Any

from pydantic import json


def get_value(data: Dict[str, Any], key: str):
    return data.get(key, None)

class ConverterService:
    vendor_mappings = {
        "Vendor21": {
            "product_name": "name",
            "price": "price",
            "description": "description",
            "image_url": "image_url"
        },
        "Vendor2": {
            "product_name": "productName",
            "price": "price.amount",
            "description": "productInfo.description",
            "image_url": "productInfo.image"
        },
        "Vendor3": {
            "product_name": "title",
            "price": "cost",
            "description": "details",
            "image_url": "image_link"
        }
    }

    @staticmethod
    def convert_to_product(vendor_data: dict, vendor_name: str):
        mapping = ConverterService.vendor_mappings.get(vendor_name)
        if not mapping:
            print(f"No mapping found for vendor {vendor_name}")
            return []

        products = []
        for item in vendor_data:
            product_data = {
                "product_name": get_value(item, mapping.get("product_name", "")),
                "description": get_value(item, mapping.get("description", "")),
                "price": get_value(item, mapping.get("price", "")),
                "image_url": get_value(item, mapping.get("image_url", ""))
            }
            products.append(product_data)
        return products
