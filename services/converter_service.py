from typing import Dict, Any


def get_value(data: Dict[str, Any], key: str):
    return data.get(key, None)

class ConverterService:
    vendor_mappings = {
        "Vendor1": {
            "product_name": "name",
            "price": "price",
            "description": "description",
            "image_url": "image_url"
        },
        "Vendor 2": {
            "product_name": "productName",
            "price": "priceAmount",
            "description": "productDescription",
            "image_url": "productImageUrl"
        },
        "Fakestore": {
            "product_name": "title",
            "price": "price",
            "description": "description",
            "image_url": "image"
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


def convert_data_for_vendor(payload: dict, vendor_name: str) -> dict:
    mapping = ConverterService.vendor_mappings.get(vendor_name)

    if not mapping:
        print(f"Mapping for vendor {vendor_name} not found!")
        return None

    product_data = {}
    for field, kafka_field in mapping.items():
        if kafka_field in payload:
            product_data[field] = payload[kafka_field]
        else:
            print(f"Missing field {kafka_field} in payload")
            product_data[field] = None

    return product_data
