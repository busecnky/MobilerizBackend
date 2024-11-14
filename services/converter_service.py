from itertools import product

from utils.mapping_utils import load_vendor_mapping, get_nested_value


class ConverterService:
    vendor_mappings = load_vendor_mapping()

    @staticmethod
    def convert_to_product(vendor_data: dict, vendor_name: str):
        if vendor_name not in ConverterService.vendor_mappings:
            print(f"No mapping found for vendor {vendor_name}")
            raise KeyError(f"Mapping for vendor '{vendor_name}' not found")

        mapping = ConverterService.vendor_mappings[vendor_name]

        products = []
        for item in vendor_data:
            product_data = {
                "product_name": get_nested_value(item, mapping["name"]),
                "description": get_nested_value(item, mapping.get("description", "")),
                "price": get_nested_value(item, mapping["price"]),
                "image_url": get_nested_value(item, mapping.get("image_url"))
            }
            products.append(product_data)
        return products





