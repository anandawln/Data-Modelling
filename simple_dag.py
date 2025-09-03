from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

# function
def hello_airflow():
    print("hello from airflow!")

# default args
default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# initialization DAG
with DAG(
    dag_id='simple_hello_dag',
    default_args=default_args,
    description='Simple DAG example',
    start_date=datetime(2025, 9, 4),
    schedule_interval='daily',
    catchup=False,
    tags['example'],
) as dag:

    task_hello = PythonOperator(
        task_id='say_hai',
        python_callable=hello_airflow
    )

    task_hello
