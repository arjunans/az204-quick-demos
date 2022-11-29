from azure.identity import ClientSecretCredential
from azure.storage.blob import BlobServiceClient

class BlobService:
    def __init__(self):
        self.TENANT_ID = "b2c7b8cb-f235-4d8a-9c9d-03561ea73ee4"
        self.CLIENT = "4a267251-714e-47d7-9a36-26a9e2fca50e"
        self.KEY = "X2S8Q~GLeGyk~DVDxDxuOJjSLpLvItlbV1pQTa3q"
        self.ACCOUNT_NAME = "stgaxisbank"
        self.CONTAINER_NAME = "container1"
        self.RESOURCE = "https://storage.azure.com/"

    def show(self):
        credentials = ClientSecretCredential(self.TENANT_ID, self.CLIENT, self.KEY)
        blobService = BlobServiceClient("https://{}.blob.core.windows.net".format(self.ACCOUNT_NAME),
                                        credential=credentials)
        print("\nList blobs in the container")
        container = blobService.get_container_client(self.CONTAINER_NAME)
        for blob in container.list_blobs():
            print("\t Blob name: " + blob.name)
