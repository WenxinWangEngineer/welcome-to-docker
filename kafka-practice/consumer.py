from kafka import KafkaConsumer


# Initialize the consumer
consumer = KafkaConsumer(
    'test-topic',
    bootstrape_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='test-group'
)


# Consume messages
for message in consumer:
    print(f"Received message: {message.value.decode('utf-8')}")
