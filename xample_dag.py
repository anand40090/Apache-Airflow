from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

# Define default_args dictionary to specify the default parameters of the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Instantiate a DAG with the DAG ID and default_args
dag = DAG(
    'example_dag',
    default_args=default_args,
    description='A simple example DAG',
    schedule_interval=timedelta(days=1),  # Run the DAG daily
)

# Define a task using BashOperator
task_hello_world = BashOperator(
    task_id='hello_world',
    bash_command='echo "Hello, World!"',
    dag=dag,
)

# Set task dependencies (if any)
# task_hello_world >> another_task

if __name__ == "__main__":
    dag.cli()
