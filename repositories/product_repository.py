from sqlalchemy.orm import Session
from models.product import Product


def create_product(db: Session, product_data: dict, vendor_id: int):
    product = Product(
        product_name=product_data["name"],
        description=product_data["description"],
        price=product_data["price"],
        image_url=product_data["image_url"],
        vendor_id=vendor_id
    )
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

def get_all_products(db: Session):
    products = db.query(Product).all()
    return products