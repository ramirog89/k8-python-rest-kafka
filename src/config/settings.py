import os

mongodb_uri         = os.getenv("MONGODB_URI", "mongodb://mongodb_user:mongodb_pass@192.168.49.2:30010")
postgres_uri        = os.getenv("POSTGRES_URI", "postgresql://ps_test:ps_passtest@192.168.49.2:30011/ps_db")
kafka_broker_server = os.getenv("KAFKA_BROKER_SERVER", "localhost:9092")
kafka_topic         = os.getenv("KAFKA_TOPIC", "events")