from kafka import KafkaProducer


# Initialize the Producer
producer = KafkaProducer(bootstrap_servers='localhost:9092')


# Send a message
producer.send('test-topic', b'Hello, Kafka!')
producer.flush()

print("Message sent!")
