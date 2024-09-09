# Purpose:
#
# Python function that connects to Snowflake
# and inserts this data into a table called user_events.
#
# Assume that each event contains fields like
# user_id, event_type, event_timestamp, and metadata.


import snowflake.connector  # type: ignore


# Function to insert event to Snowflake
def insert_event_to_snowflake(event_data):
    # establish the connection to Snowflake
    conn = snowflake.connector.connect(
        user='YOUR_USERNAME',
        password='YOUR_PASSWORD',
        account='YOUR_ACCOUNT',
        warehouse='YOUR_WAREHOUSE',
        schema='YOUR_SCHEMA',
        table='YOUR_TABLE'
    )

    cursor = conn.cursor()

    # SQL query to insert data
    insert_query = """
    INSERT INTO user_events(user_id, event_type, event_timestamp, metadata)
    VALUES(%(user_id)s, %(event_type)s, %(event_timestamp)s, %(metadata)s)
    """

    # Execute the query with event data
    cursor.execute(insert_query, {
        'user_id': event_data['user_id'],
        'event_type': event_data['event_type'],
        'event_timestamp': event_data['event_timestamp'],
        'metadata': event_data['metadata']
    })

    # Commit the transaction and close the connection
    conn.commit()
    cursor.close()
    conn.close()
