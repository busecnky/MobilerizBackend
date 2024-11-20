from sqlalchemy.orm import Session

from config.kafka_config import get_kafka_consumer
from models.product import Product


def consume_messages_from_kafka(db: Session, product_name: str):
    consumer = get_kafka_consumer()

    try:
        for message in consumer:

            payload = message.value
            payload_data = payload['product']

            try:
                product_name_from_kafka = payload_data["product_name"]
                if product_name_from_kafka == product_name:

                    save_data_to_sqlite(db, payload_data)

                break
            except Exception as e:
                print(f"Missing key in product data: {e}")

    except Exception as e:
        print(f"Error while consuming messages from Kafka: {e}")

    finally:
        consumer.close()

def save_data_to_sqlite(db: Session, payload: dict):

    try:
        new_product = Product(
            product_name=payload["product_name"],
            price=payload["price"],
            description=payload["description"],
            image_url=payload["image_url"],
            vendor_id=payload["vendor_id"]
        )

        db.add(new_product)
        db.commit()
        db.refresh(new_product)
        print(f"Product saved to SQLite: {new_product.product_name}")

    except Exception as e:
        print(f"Error while saving to SQLite: {e}")
        db.rollback()
