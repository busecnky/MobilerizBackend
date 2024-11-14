from sqlalchemy.orm import Session
from models.product import Product


def create_product(db: Session, data: dict, vendor_id: int):
    product = Product(
        name=data['name'],
        price=data['price'],
        description=data['description'],
        image_url=data['image_url'],
        vendor_id=vendor_id,
    )
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

def get_all_products(db: Session):
    products = db.query(Product).all()
    return products