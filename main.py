import google.generativeai as genai
from config import GOOGLE_API_KEY

def list_ai_models():
    genai.configure(api_key=GOOGLE_API_KEY)
    
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)

if __name__ == "__main__":
    list_ai_models()
            