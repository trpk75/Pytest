import azure.functions as func
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

def main(req: func.HttpRequest) -> func.HttpResponse:

    connection_string = "https://infgsbuxblob.blob.core.windows.net/testblobcontainer/evblob?sp=r&st=2024-02-14T11:23:31Z&se=2024-03-01T19:23:31Z&spr=https&sv=2022-11-02&sr=b&sig=%2FoBjEExFPVQaTi9ITJTy43X35m2E2Fyw%2BQObK8AqWHM%3D"

    try:
        # Create a BlobServiceClient object which will be used to create a ContainerClient and BlobClient
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        
        # Create a blob client using the blob_name
        blob_client = blob_service_client.get_blob_client(container="testblobcontainer", blob="evblob")
        
        # Download blob content
        blob_data = blob_client.download_blob().readall()
        
        return func.HttpResponse(blob_data, status_code=200)
    
    except Exception as e:
        return func.HttpResponse(f"An error occurred: {str(e)}", status_code=500)
