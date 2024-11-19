import json

from kafka import KafkaProducer, KafkaConsumer

KAFKA_BROKER_URL = "localhost:29092"
TOPIC_NAME = "mobileriz_topic"
DEBEZIUM_TOPIC_NAME = "dbserver1.public.products"

def get_kafka_producer():
    return KafkaProducer(
        bootstrap_servers=KAFKA_BROKER_URL,
        value_serializer=lambda v: json.dumps(v).encode("utf-8")
    )

def get_kafka_consumer():
    return KafkaConsumer(
        TOPIC_NAME,
        bootstrap_servers=KAFKA_BROKER_URL,
        auto_offset_reset="earliest",
        enable_auto_commit=True,
        group_id="kafka-group",
        value_deserializer=lambda x: json.loads(x.decode("utf-8"))
    )

def get_debezium_consumer():
    return KafkaConsumer(
        DEBEZIUM_TOPIC_NAME,
        bootstrap_servers=KAFKA_BROKER_URL,
        auto_offset_reset="earliest",
        enable_auto_commit=True,
        group_id="debezium-group",
        value_deserializer=lambda x: json.loads(x.decode("utf-8"))
    )
