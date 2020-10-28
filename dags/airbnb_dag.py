
from datetime import timedelta

from airflow import DAG
from airflow import models

from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from utils.storage import StorageHook
from utils import config

from utils import FILE_NAMES, GITHUB_BASE_URL_DOWNLOAD

yaml_config = config.get_yaml_config()
dag_config = yaml_config['dags']['airbnb']

default_args = {
    'owner': 'França',
    'start_date': dag_config['start_date'],
    'retries': dag_config['retries'],
    'retry_delay': timedelta(minutes=dag_config['retry_delay_minutes']),
}

if __name__ == "__main__":
    with models.DAG("elt_airbnb_dag",
                    schedule_interval=timedelta(days=1),
                    default_args=default_args,
                    description='A simple ELT pipeline example DAG') as dag:


        github_to_storage_raw = PythonOperator(
            task_id='extract_github_to_storage',
            provide_context=False,
            catchup=False,
            python_callable=StorageHook.upload_blobs,
            op_kwargs={"bucket_name": "toureyes-data-lake",
                    "file_names_list": FILE_NAMES,
                    "github_url": GITHUB_BASE_URL_DOWNLOAD,
                    "storage_folder_path": "datasprints/raw"},
            dag=dag,
        )


        storage_raw_to_refined = PythonOperator(
            task_id='storage_raw_to_refined',
            provide_context=False,
            catchup=False,
            python_callable=StorageHook.transform_blobs,
            op_kwargs={"bucket_name": "toureyes-data-lake",
                    "blobs_path": "datasprints/raw",
                    "destination_blobs_path": "datasprints/refined"},
            dag=dag,
        )

        github_to_storage_raw >> storage_raw_to_refined
