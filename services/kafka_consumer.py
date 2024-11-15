from config.kafka_config import get_kafka_consumer


def consume_messages_from_kafka():
    consumer = get_kafka_consumer()
    try:
        for message in consumer:
            print(f"Message received: {message.value}")
    except Exception as e:
        print(f"Error consuming messages: {e}")
    finally:
        consumer.close()
