from kafka import KafkaProducer, KafkaConsumer

KAFKA_BROKER_URL = "localhost:9093"
TOPIC_NAME = "mobileriz_topic"

def get_kafka_producer():
    return KafkaProducer(
        bootstrap_servers=KAFKA_BROKER_URL,
        value_serializer=lambda v: v.encode("utf-8"),
    )

def get_kafka_consumer():
    return KafkaConsumer(
        TOPIC_NAME,
        bootstrap_servers=KAFKA_BROKER_URL,
        auto_offset_reset="earliest",
        enable_auto_commit=True,
        group_id="my-group",
        value_deserializer=lambda v: v.decode("utf-8"),
    )
