from typing import List
import os
import json
import pandas as pd
import io

from google.cloud import storage
from google.oauth2 import service_account

from .utils import download_from_github_url

class StorageHook():

    # def upload_blobs(self, bucket_name: str = None, file_names_list: List[str] = None, github_url: str = None, storage_folder_path: str = None):
    def upload_blobs(**kwargs):
        bucket_name = kwargs['bucket_name']
        file_names_list = kwargs['file_names_list']
        github_url = kwargs['github_url']
        storage_folder_path = kwargs['storage_folder_path']
        """Uploads a file to the bucket."""
        # bucket_name = "your-bucket-name"
        # source_file_name = "local/path/to/file"
        # destination_blob_name = "storage-object-name"
        credentials = service_account.Credentials.from_service_account_file(
        "/home/airflow/google_credentials.json", scopes=["https://www.googleapis.com/auth/cloud-platform"],
        )

        storage_client = storage.Client(credentials=credentials, project=credentials.project_id,)
        bucket = storage_client.bucket(bucket_name)
        
        for f in file_names_list:
            content = download_from_github_url(github_url + f)
            blob = bucket.blob(storage_folder_path + "/" + f)

            blob.upload_from_string(data=content, content_type="application/json")

        print(
            "{} files uploaded to {}.".format(
                len(file_names_list), bucket_name + "/" + storage_folder_path
            )
        )


    def download_blob(**kwargs):
        """Downloads a blob from the bucket."""
        # bucket_name = "your-bucket-name"
        # source_blob_name = "storage-object-name"
        # destination_file_name = "local/path/to/file"

        bucket_name = kwargs['bucket_name']
        source_blob_name = kwargs['source_blob_name']
        
        credentials = service_account.Credentials.from_service_account_file(
        "/home/airflow/google_credentials.json", scopes=["https://www.googleapis.com/auth/cloud-platform"],
        )

        storage_client = storage.Client(credentials=credentials, project=credentials.project_id,)

        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(source_blob_name)
        # download as string
        json_data_string = blob.download_as_string()
        json_data = json.loads(json_data_string)
        airbnb = {}
        airbnb['bathrooms'] = json_data['listing']['bathrooms']
        airbnb['bedrooms'] = json_data['listing']['bedrooms']
        airbnb['beds'] = json_data['listing']['beds']
        airbnb['city'] = json_data['listing']['city']
        airbnb['lat'] = json_data['listing']['lat']
        airbnb['lng'] = json_data['listing']['lng']
        airbnb['star_rating'] = json_data['listing']['star_rating']
        airbnb['pricing_quote'] = json_data['pricing_quote']['rate']['amount']

        df = pd.DataFrame.from_records([airbnb])

        s_buf = df.to_string(None, index=False)
        blob2 = bucket.blob("airbnb/raw/refined")
        blob2.upload_from_string(s_buf)

        print(
            "Blob transformed to refined.".format(
                source_blob_name
            )
        )
