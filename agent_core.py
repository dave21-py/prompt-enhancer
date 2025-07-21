import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Gemini 1.5 Flash (fast + inexpensive)
model = genai.GenerativeModel("models/gemini-1.5-flash")

def generate_agent_response(user_prompt: str, target_model: str) -> str:
    """
    Rewrite `user_prompt` for the chosen `target_model` (ChatGPT, Claude, Gemini).
    Guarantees the return string is ONLY the enhanced prompt – never an answer.
    """

    # — System instructions per model —
    instructions = {
        "ChatGPT": (
            "SYSTEM:\n"
            "You are a ✨ Prompt‑Enhancer ✨. Rewrite the user's prompt to maximise clarity, structure, and intent for OpenAI ChatGPT.\n"
            "Do NOT answer or explain the prompt. Return ONE line: the enhanced prompt only."
        ),
        "Claude": (
            "SYSTEM:\n"
            "You are a ✨ Prompt‑Enhancer ✨ for Anthropic Claude. Rewrite the prompt to be cooperative, safe, and instruction‑rich.\n"
            "NEVER answer or elaborate. Output ONLY the rewritten prompt line."
        ),
        "Gemini": (
            "SYSTEM:\n"
            "You are a ✨ Prompt‑Enhancer ✨ for Google Gemini. Rewrite the prompt to boost context and reasoning.\n"
            "Do NOT answer the prompt. Output ONLY the rewritten prompt itself."
        )
    }

    prompt_template = (
        "{instruction}\n\n"
        "USER_PROMPT: {user}\n"
        "ENHANCED_PROMPT:"
    )

    system_instruction = instructions.get(target_model, instructions["ChatGPT"])
    full_prompt = prompt_template.format(instruction=system_instruction, user=user_prompt)

    # Call Gemini
    response = model.generate_content(full_prompt)
    text = response.text.strip()

    # — Post‑filter: remove any accidental leading phrases —
    for marker in ["ENHANCED_PROMPT:", "Enhanced Prompt:", "Rewritten Prompt:", "Sure", "Here is", "Here’s"]:
        if text.lower().startswith(marker.lower()):
            text = text.split(":", 1)[-1].strip()

    # Final single‑line enhanced prompt
    return text
