from kafka import KafkaConsumer
import json


# Initialize kafka consumer
consumer = KafkaConsumer(
    'user_events',  # topic
    bootstrap_servers=['localhost:9092'],  # server details
    auto_offset_reset='earlist',  # start reading from the earlist message
    enable_auto_commit=True,  # automatically commit message offsets
    group_id='user-event-consumers',  # consumer group
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    # deserialize JSON messages
)


# Process each message
for message in consumer:
    event_data = message.value
    print(f"Processing event: {event_data}")

    # Assuming Snowflake insertion logic comes next
