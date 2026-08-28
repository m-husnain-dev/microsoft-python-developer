import os
from azure.storage.blob import BlobServiceClient

# Connection string setup
CONNECTION_STRING = "YOUR_AZURE_STORAGE_CONNECTION_STRING"
CONTAINER_NAME = "my-sample-container"

# 1. Client initialize karein
blob_service_client = BlobServiceClient.from_connection_string(
    CONNECTION_STRING
)

# 2. Container create karein (agar maujood na ho)
try:
    container_client = blob_service_client.create_container(CONTAINER_NAME)
    print(f"Container '{CONTAINER_NAME}' created successfully.")
except Exception as e:
    container_client = blob_service_client.get_container_client(CONTAINER_NAME)
    print(f"Container '{CONTAINER_NAME}' already exists.")

# 3. File upload karein
file_to_upload = "sample.txt"
with open(file_to_upload, "w") as f:
    f.write("Hello Azure Blob Storage from Python!")

blob_client = container_client.get_blob_client(file_to_upload)
with open(file_to_upload, "rb") as data:
    blob_client.upload_blob(data, overwrite=True)
print(f"File '{file_to_upload}' uploaded to Azure Blob Storage.")