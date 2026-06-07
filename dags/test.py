from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def hello():
    print("Hello, Airflow!")

with DAG(
    'test_dag',
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False
) as dag:
    test_task = PythonOperator(
        task_id='hello_task',
        python_callable=hello
    )
