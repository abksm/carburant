from datetime import timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from carburants_request import extract_data

start_date = datetime(2023, 11, 20, 12, 00)

default_args = {
    'owner': 'admin',
    'start_date': start_date,
    'retries': 5,
    'retry_delay': timedelta(seconds=30)
}

with DAG('carburants_request', default_args=default_args, schedule_interval='*/10 * * * *', catchup=False) as dag:

    craburant_request_task = PythonOperator(
        task_id='carburants_request',
        python_callable=extract_data,
        dag=dag,
        )

