from pydantic import BaseModel


class VendorData(BaseModel):
    vendor_name: str
    base_url: str
