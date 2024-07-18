import google.generativeai as genai
from google.cloud import storage
from config import GEN_AI_KEY, GCP_PROJECT_NAME

def list_ai_models():
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

if __name__ == "__main__":
    list_ai_models()
    interact_with_gcs()
            