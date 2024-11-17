from config.kafka_config import get_kafka_producer, TOPIC_NAME


def send_message_to_kafka(message: dict):
    producer = get_kafka_producer()
    try:
        producer.send(TOPIC_NAME, value=message)
        producer.flush()
        print(f"Message sent: {message}")
    except Exception as e:
        print(f"Error sending message: {e}")
    finally:
        producer.close()
