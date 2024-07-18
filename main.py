import base64
import google.generativeai as genai
from google.cloud import storage
from config import GEN_AI_KEY, GCP_PROJECT_NAME, GCP_BUCKET_NAME

def configure_ai():
    genai.configure(api_key=GEN_AI_KEY)
    
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)
        
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

def get_image_from_bucket(bucket_name, blob_name):
    storage_client = storage.Client(project=GCP_PROJECT_NAME)
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    
    image_bytes = blob.download_as_bytes()
    return image_bytes

def analyze_image_with_genai(image_bytes):
    model = genai.GenerativeModel('gemini-pro-vision')
    
    # Convert image bytes to base64
    image_base64 = base64.b64encode(image_bytes).decode('utf-8')
    
    # Create a parts list with the image
    parts = [
        {
            "mime_type": "image/jpeg",
            "data": image_base64
        },
        {
            "text": "Describe this image in detail."
        }
    ]
    
    # Generate content
    response = model.generate_content(parts)
    
    return response.text

if __name__ == "__main__":
    configure_ai()
    # interact_with_gcs()
    # create_bucket(GCP_BUCKET_NAME)
    # upload_file(GCP_BUCKET_NAME, 'jg-mugshot.jpeg', 'jg-mushot.jpeg')
    
    # Get the image from the GCP bucket
    image_bytes = get_image_from_bucket(GCP_BUCKET_NAME, 'jg-mushot.jpeg')
    
    # Analyze the image using genai
    description = analyze_image_with_genai(image_bytes)
    
    print("Image Description:")
    print(description)