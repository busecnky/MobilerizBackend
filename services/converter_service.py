from itertools import product

from utils.mapping_utils import load_vendor_mapping, get_nested_value


class ConverterService:
    vendor_mappings = load_vendor_mapping()

    @staticmethod
    def convert_to_product(vendor_data: dict):
        mapping = ConverterService.vendor_mappings[vendor_data['name']]
        if not mapping:
            print (f"No mapping found for vendor {vendor_data['name']}")

        products = []
        for item in vendor_data:
            product_data = {
                "name": get_nested_value(item, mapping["name"]),
                "description": get_nested_value(item, mapping.get("description", "")),
                "price": get_nested_value(item, mapping["price"]),
                "image_url": get_nested_value(item, mapping.get("image"))
            }
            products.append(product_data)
        return products





