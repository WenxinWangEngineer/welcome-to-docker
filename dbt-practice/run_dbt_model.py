import subprocess

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago


def run_dbt_model():
    # Run the DBT model using subprocess
    result = subprocess.run(['dbt', 'run', '--models', 'my-model'], capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f"DBT run failed: {result.stderr}")
    print(result.stdout)


# Define teh default_args
default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
    'retries': 1
}


# Define the DAG
dag = DAG(
    'dbt_model_dag',
    default_args=default_args,
    description='A DAG to run a DBT model',
    schedule_interval='@daily',
)


# Define the task
run_dbt_task = PythonOperator(
    task_id='run_dbt_model',
    python_callable=run_dbt_model,
    dag=dag
)


run_dbt_task
