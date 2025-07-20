from dotenv import load_dotenv
load_dotenv()
import gradio as gr
from agent_core import generate_agent_response

# --- New respond() function: Enhances prompt instead of replying ---
def respond(message, chat_history, target_model):
    # Append original user prompt
    chat_history.append({"role": "user", "content": message})

    # Get enhanced prompt based on target model
    enhanced_prompt = generate_agent_response(message, target_model)

    # Append enhanced version as assistant output
    chat_history.append({"role": "assistant", "content": enhanced_prompt})

    return "", chat_history

# --- Gradio UI ---
with gr.Blocks(title="Prompt Enhancer") as demo:
    gr.Markdown("## ✨ Prompt Enhancer — Fine-tune your prompts like a pro!")

    # Updated from "role" to "target_model"
    target_model = gr.Radio(
        ["ChatGPT", "Claude", "Gemini"],
        label="Choose Enhancement Target",
        value="ChatGPT"
    )

    # Chat UI - Shows original vs enhanced prompts
    chatbot = gr.Chatbot(type='messages', label="Prompt Enhancement History")

    # Input textbox
    msg = gr.Textbox(placeholder="Enter your original prompt here...", label="Original Prompt")

    # Clear button
    clear = gr.Button("Clear History")

    # Submit to trigger enhancement
    msg.submit(respond, [msg, chatbot, target_model], [msg, chatbot])
    clear.click(lambda: ([], ""), None, [chatbot, msg], queue=False)

    gr.Markdown("Crafted with ⚡ by Dave — using Google Gemini API")

demo.launch()
