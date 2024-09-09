# Purpose:
#
# Create an Airflow Dag that runs a daily task to fetch data from Snowflake,
# process it,
# and store back to another table.
from airflow import DAG
from airflow.operators.python_operator import PythonOperator  # type: ignore
from datetime import datetime
import snowflake.connector  # type: ignore


# Define the DAG and its schedule (daily)
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 9, 9),
    'retries': 1
}
dag = DAG(
    'snowflake_etl',
    default_args=default_args, schedule_interval='@daily'
    )


# Funciton to extract data from Snowflake
def extract_data():
    conn = snowflake.connector(
        user='YOUR_USERNAME',
        password='YOUR_PASSWORD',
        account='YOUR_ACCOUNT',
        warehouse='YOUR_WAREHOUSE',
        database='YOUR_DATABASE',
        schema='YOUR_SCHEMA'
    )
    cursor = conn.cursor()

    # Extract data from raw_user_events table
    cursor.execute(
        "SELECT * FROM raw_user_events WHERE event_type = 'video_play'"
        )
    results = cursor.fetchall()

    cursor.close()
    conn.close()

    return results


# Function to transform data
def transform_data(**contents):
    raw_data = contents['ti'].xcom_pull(task_ids='extract')

    # Filter data based on a condition (if not done in Snowflake query)
    transformed_data = [row for row in raw_data if row[1] == 'video_play']

    return transformed_data


# Function to load data back to another table
def load_data(**contents):
    transformed_data = contents['ti'].xcom_pull(task_ids='transform')

    conn = snowflake.connector.connect(
        user='YOUR_USERNAME',
        password='YOUR_PASSWORD',
        account='YOUR_ACCOUNT',
        warehouse='YOUR_WAREHOUSE',
        database='YOUR_DATABASE',
        schema='YOUR_SCHEMA'
    )
    cursor = conn.cursor()

    # Insert transformed data into filtered_user_events table
    insert_query = """
    INSERT INTO filtered_user_events (
        user_id, event_type, event_timestamp, metadata)
    VALUES (%s, %s, %s, %s)
    """

    for row in transformed_data:
        cursor.execute(insert_query, row)

    conn.commit()
    cursor.close()
    conn.close()


# Define tasks
extract_task = PythonOperator(
    task_id='extract',
    python_callable=extract_data,
    dag=dag
)

transform_task = PythonOperator(
    task_id='transform',
    python_callable=transform_data,
    provide_context=True,
    dag=dag
)

load_task = PythonOperator(
    task_id='load',
    python_callable=load_data,
    providd_context=True,
    dag=dag
)


# Set task dependencies
extract_task >> transform_task >> load_task
