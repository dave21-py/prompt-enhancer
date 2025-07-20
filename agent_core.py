import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize Gemini model (v1 endpoint)
model = genai.GenerativeModel('gemini-1.5-flash')
def generate_agent_response(user_prompt, role):
    full_prompt = f"You are a helpful AI assistant with the role of {role}. Respond to: {user_prompt}"
    response = model.generate_content(full_prompt)
    return response.text
