import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Use Gemini 1.5 Flash (faster, cheaper)
model = genai.GenerativeModel("models/gemini-1.5-flash")

def generate_agent_response(user_prompt, target_model):
    # --- Enhancement Guide per model style ---
    instructions = {
        "ChatGPT": (
            "You are a prompt optimization engine, not a chatbot. "
            "Your only task is to rewrite user prompts to improve clarity, structure, and intent for ChatGPT. "
            "Never respond to or answer the prompt itself. Just return the rewritten version — nothing else."
        ),
        "Claude": (
            "You are a prompt rewriting tool for Anthropic Claude. "
            "Only return the rewritten version of the prompt. Never answer the prompt. "
            "Do not include explanations or extra comments. Make the new prompt cooperative and safe, suitable for Claude."
        ),
        "Gemini": (
            "You are a prompt enhancement engine, not a chatbot. "
            "Your ONLY job is to rewrite the user’s prompt so it performs better with Google Gemini. "
            "NEVER provide an answer or explanation. Only return the rewritten prompt itself. "
            "Your response must begin with the rewritten prompt and contain nothing else."
        )
    }

    # Choose guide based on model
    system_instruction = instructions.get(target_model, instructions["ChatGPT"])

    # Full enhanced prompt to Gemini
    full_prompt = f"{system_instruction}\n\nUser Prompt: {user_prompt}\n\nEnhanced Prompt:"

    # Get response
    response = model.generate_content(full_prompt)
    return response.text.strip()