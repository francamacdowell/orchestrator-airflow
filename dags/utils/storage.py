from google.cloud import storage
import os

class StorageHook():

    def upload_blobs(bucket_name, folder_path, storage_folder_path):
        """Uploads a file to the bucket."""
        # bucket_name = "your-bucket-name"
        # source_file_name = "local/path/to/file"
        # destination_blob_name = "storage-object-name"
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        file_names_list = os.listdir(folder_path)
        
        for f in file_names_list:
            
            blob = bucket.blob(storage_folder_path + f)

            blob.upload_from_filename(folder_path + f)

        print(
            "{} files uploaded to {}.".format(
                len(file_names_list), bucket_name + storage_folder_path
            )
        )
