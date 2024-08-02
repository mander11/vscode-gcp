import google.generativeai as genai

# Replace with your actual API key
# https://aistudio.google.com/app/apikey
genai.configure(api_key='<API_KEY>')  

model = genai.GenerativeModel('gemini-1.5-pro')

# Generate content
response = model.generate_content(
    "Why is the sky blue?",
    generation_config=genai.types.GenerationConfig(
        temperature=0.9,
        top_p=1,
        top_k=1,
        max_output_tokens=2048,
    ),
    safety_settings={
        genai.types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: genai.types.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE
    }
)

print(response.text)