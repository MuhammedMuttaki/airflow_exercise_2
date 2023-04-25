from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator

def python_datetime_func():
    # datetime object containing current date and time
    current_datetime = datetime.now()
    print("Current Date and Time =", current_datetime)

default_dag_args = {
    'start_date': datetime(2023, 4, 25),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries':1,
    'retry_delay': timedelta(minutes=5),
    'project_id':1
}

with DAG("python_task_DAG", schedule_interval = '@daily', catchup = False, default_args = default_dag_args) as dag_python:
    
    task_0 = PythonOperator(task_id = 'python_task', python_callable = python_datetime_func)