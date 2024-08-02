import google.auth
from google.auth.transport import requests
import google.auth.transport.requests
import requests
import json

PROJECT_ID = "manderson-code-retreat-prep"
LOCATION = "us-east1"

# Authenticate
credentials, _ = google.auth.default()
auth_request = google.auth.transport.requests.Request()
credentials.refresh(auth_request)

# Set up the API endpoint
API_ENDPOINT = f"https://{LOCATION}-aiplatform.googleapis.com/v1/projects/{PROJECT_ID}/locations/{LOCATION}/publishers/google/models/gemini-1.5-pro:generateContent"

# Set up the headers
headers = {
    "Authorization": f"Bearer {credentials.token}",
    "Content-Type": "application/json"
}

# Set up the request payload
payload = {
    "contents": [
        {
            "role": "user",
            "parts": [{"text": "Why is the sky blue?"}]
        }
    ],
    "safety_settings": [
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        }
    ],
    "generation_config": {
        "temperature": 0.9,
        "topP": 1,
        "topK": 1,
        "maxOutputTokens": 2048,
    }
}

# Make the API request
response = requests.post(API_ENDPOINT, headers=headers, json=payload)

# Check if the request was successful
if response.status_code == 200:
    # Parse the response
    response_data = response.json()
    print(json.dumps(response_data, indent=2))
else:
    print(f"Error: {response.status_code}")
    print(response.text)