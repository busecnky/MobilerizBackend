import json
import os
from pathlib import Path

from pyflink.datastream import StreamExecutionEnvironment, RuntimeExecutionMode
from pyflink.datastream.connectors.kafka import FlinkKafkaConsumer, FlinkKafkaProducer

os.environ['FLINK_HOME'] = 'C:/Flink/opt'
BASE_DIR = Path(__file__).resolve().parent.parent
jars_path = BASE_DIR / "jar_files" / "flink-sql-connector-kafka-3.3.0-1.20.jar"

def process_data(request):
    request["price"] = round(request["price"] * 1.1, 2)
    return request

def flink_pipeline():
    env = StreamExecutionEnvironment.get_execution_environment()
    env.set_runtime_mode(RuntimeExecutionMode.BATCH)
    env.set_parallelism(1)
    env.add_jars(f"file://{jars_path}")

    consumer = FlinkKafkaConsumer(
        topics="mobileriz_topic",
        properties={"bootstrap.servers": "kafka:9092"},
        deserialization_schema=lambda x: json.loads(x.decode("utf-8"))
    )
    producer = FlinkKafkaProducer(
        topic="unified_data",
        producer_config={"bootstrap.servers": "kafka:9092"},
        serialization_schema=lambda x: json.dumps(x).encode("utf-8")
    )

    stream = env.add_source(consumer)
    stream.print()
    processed_stream = stream.map(process_data)
    processed_stream.add_sink(producer)

    env.execute("Flink Data")

if __name__ == "__main__":
    flink_pipeline()