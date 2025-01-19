from kafka import KafkaProducer
import random
import time

producer = KafkaProducer(bootstrap_servers=['127.0.0.1:9092', '127.0.0.1:9093', '127.0.0.1:9094'], acks="all")

iid = 0
available_keys = [b"kafka_chat_1", b"kafka_chat_2", b"kafka_chat_3", b"kafka_chat_4", b"kafka_chat_5"]

while True:
    use_key = random.choice(available_keys)  # Choose a random key.

    # Message to deliver.
    msg = f"{time.time()}: message {iid} with key {use_key.decode('utf-8')} from producer!"
    confirmation = producer.send('kafka-chat', value=str.encode(msg), key=use_key)

    try:
        confirmation.get()
        print(f"Successfully produced {msg}!")
    except Exception:
        print(f"Failed to deliver {msg}")

    iid += 1
    time.sleep(1)
