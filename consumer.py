from kafka import KafkaConsumer
consumer = KafkaConsumer(
    "kafka-chat",
    bootstrap_servers = ['127.0.0.1:9092', '127.0.0.1:9093', '127.0.0.1:9094'],
)
for msg in consumer:
    print(f"Consumed message from partition {msg.partition}: {msg.value.decode('utf-8')}")
