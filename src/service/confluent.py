import threading
import logging

from confluent_kafka import Consumer, KafkaError, KafkaException
from src.config.settings import kafka_broker_server, kafka_topic

logger = logging.getLogger("debug")

consumer = Consumer({
    'bootstrap.servers': kafka_broker_server,
    'group.id': 'python-demo'
})

def consume_loop():
    try:
        consumer.subscribe([kafka_topic])

        print("Kafka is listening.")

        while True:
            msg = consumer.poll(timeout=1.0)
            if msg is None:
                continue

            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    logger.error('%% %s [%d] reached end at offset %d\n' %
                                     (msg.topic(), msg.partition(), msg.offset()))
                elif msg.error():
                    raise KafkaException(msg.error())
            else:
                logger.info(f"Kafka message recived: {msg.value()}")
    finally:
        logger.error("Kafka Closed connection")
        # Close down consumer to commit final offsets.
        consumer.close()

def listen_kafka_messages():
    kafka_thread = threading.Thread(target=consume_loop)
    kafka_thread.setDaemon(True)
    kafka_thread.start()
