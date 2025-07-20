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
            "You are an expert in prompting OpenAI's ChatGPT. "
            "Given the user input, rewrite the prompt to maximize clarity, intent, and reasoning. "
            "Only rewrite the prompt. Do not answer it. Return only the enhanced prompt."
        ),
        "Claude": (
            "Your task is to enhance user prompts to make them more effective for Anthropic Claude — "
            "but you must NOT answer, expand upon, or explain the prompt. "
            "Return only a rewritten version of the prompt that is more clear, precise, instruction-rich, and aligned with Claude’s style. "
            "Start the response directly with the enhanced prompt. Do not include any introductions or disclaimers."
        ),
        "Gemini": (
            "You are an expert in prompting Google's Gemini. "
            "You are optimizing this prompt for Google Gemini. "
            "DO NOT respond to the prompt. DO NOT provide an answer or explanation. "
            "ONLY return an improved, enhanced version of the original prompt. "
            "Focus on improving clarity, completeness, and multi-turn reasoning. "
        )
    }

    # Choose guide based on model
    system_instruction = instructions.get(target_model, instructions["ChatGPT"])

    # Full enhanced prompt to Gemini
    full_prompt = f"{system_instruction}\n\nUser Prompt: {user_prompt}\n\nEnhanced Prompt:"

    # Get response
    response = model.generate_content(full_prompt)
    return response.text.strip()
