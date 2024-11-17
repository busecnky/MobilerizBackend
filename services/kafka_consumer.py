from config.kafka_config import get_kafka_consumer
from config.sqlite_config import get_db


def consume_messages_from_kafka():
    consumer = get_kafka_consumer()
    try:
        db = next(get_db())
        for message in consumer:
            print(f"Message received: {message.value}")
    except Exception as e:
        print(f"Error consuming messages: {e}")
    finally:
        consumer.close()
