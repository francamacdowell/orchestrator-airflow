
from datetime import timedelta

from airflow import DAG

from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from utils.storage import StorageHook
from utils.config import get_yaml_config


yaml_config = get_yaml_config()
dag_config = yaml_config['dags']['airbnb']

default_args = {
    'owner': 'França',
    'start_date': dag_config['start_date'],
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': dag_config['retries'],
    'retry_delay': timedelta(minutes=dag_config['retry_delay_minutes']),
}

dag = DAG(
    'elt_airbnb_dag',
    default_args=default_args,
    schedule_interval=timedelta(days=dag_config['schedule_interval_days']),
)


with DAG("elt_airbnb_dag",
                description='A simple ELT pipeline example DAG',
                schedule_interval=timedelta(days=1),
                default_args=default_args) as dag:

    run_this = PythonOperator(
        task_id='print_the_context',
        provide_context=True,
        python_callable=StorageHook.upload_blobs,
        op_args=[bucket_name, folder_path, storage_folder_path],
        dag=dag,
    )