import requests
import json

# Kafka Connect'in REST API URL'si
url = 'http://localhost:8083/connectors'

# Debezium konfigürasyon dosyasındaki JSON içeriği
debezium_config = {
    "name": "my-postgres-connector",
    "config": {
        "connector.class": "io.debezium.connector.postgresql.PostgresConnector",
        "database.hostname": "localhost",
        "database.port": "5432",
        "database.user": "user",
        "database.password": "4628",
        "database.dbname": "mobilerizDB",
        "database.server.name": "dbserver1",
        "plugin.name": "pgoutput",
        "slot.name": "debezium",
        "publication.name": "debezium_pub",
        "table.include.list": "public.products",
        "transforms": "unwrap",
        "transforms.unwrap.type": "io.debezium.transforms.ExtractNewRecordState",
        "topic.prefix": "dbserver1"
    }
}

# POST isteği gönder
response = requests.post(url, headers={'Content-Type': 'application/json'}, data=json.dumps(debezium_config))

# Yanıtı yazdır
if response.status_code == 201:
    print("Connector successfully created!")
else:
    print(f"Failed to create connector: {response.status_code}, {response.text}")
