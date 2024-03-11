import asyncio
import aiokafka
import logging

from src.config.settings import kafka_broker_server, kafka_topic

loop = asyncio.get_event_loop()
logger = logging.getLogger("debug")

async def consume():
    consumer = aiokafka.AIOKafkaConsumer(
        kafka_topic,
        loop=loop,
        bootstrap_servers=kafka_broker_server
    )

    logger.info(f"Consumer started, listening on topic: {kafka_topic}")

    try:
        await consumer.start()
    except Exception as e:
        logger.error(f"Kafka exception: {e}")
        return

    try:
        async for msg in consumer:
            logger.info("Kafka message: topic={}:{:d}:{:d}: key={} value={} timestamp_ms={}".format(msg.topic, msg.partition, msg.offset, msg.key, msg.value, msg.timestamp))
    finally:
        await consumer.stop()


def listen_kafka_messages():
    asyncio.create_task(consume())
