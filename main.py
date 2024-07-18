import google.generativeai as genai
from google.cloud import storage
from config import GEN_AI_KEY, GCP_PROJECT_NAME, GCP_BUCKET_NAME

def configure_ai():
    genai.configure(api_key=GEN_AI_KEY)
    
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)

def interact_with_gcs():
    storage_client = storage.Client(project=GCP_PROJECT_NAME)

    print("Listing buckets:")
    buckets = storage_client.list_buckets()
    for bucket in buckets:
        print(bucket.name)
        
def create_bucket(bucket_name):
    storage_client = storage.Client(project=GCP_PROJECT_NAME)
    bucket = storage_client.create_bucket(bucket_name)
    print(f"Bucket {bucket.name} created.")
    
def upload_file(bucket_name, source_file_name, destination_blob_name):
    storage_client = storage.Client(project=GCP_PROJECT_NAME)
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(f"File {source_file_name} uploaded to {destination_blob_name} in bucket {bucket_name}.")


if __name__ == "__main__":
    configure_ai()
    # interact_with_gcs()
    # create_bucket(GCP_BUCKET_NAME)
    # upload_file(GCP_BUCKET_NAME, 'jg-mugshot.jpeg', 'jg-mushot.jpeg')
    