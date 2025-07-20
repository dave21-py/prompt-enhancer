from dotenv import load_dotenv
load_dotenv()
import gradio as gr
from agent_core import generate_agent_response

# --- FUNCTION CORRECTED ---
# 1. Removed the unnecessary `with gr.Row()` context manager.
# 2. Changed how messages are appended to the history to match the new format.
def respond(message, chat_history, role):
    # Append the user's message to the history in the new dictionary format
    chat_history.append({"role": "user", "content": message})
    
    # Get the agent's response
    response = generate_agent_response(message, role)
    
    # Append the agent's response to the history
    chat_history.append({"role": "assistant", "content": response})
    
    # Return an empty string to clear the textbox, and the updated history
    return "", chat_history

with gr.Blocks(title="Mini Agent Builder") as demo:
    gr.Markdown("## 🤖 Prompt Enhancer — Powered by Google Gemini")

    role = gr.Radio(["helpful", "sarcastic", "genz"], label="Choose Agent Style", value="helpful")

    # The `state` component will now hold our history in the new format.
    # It's better to use the chatbot component itself to store state in this new format.
    chatbot = gr.Chatbot(type='messages', label="Chatbot") 
    
    msg = gr.Textbox(placeholder="Type your message...", label="Your Message")
    
    # --- CLEAR BUTTON IMPROVED ---
    # The clear button now resets both the chatbot display and the message box.
    clear = gr.Button("Clear Chat")

    # The submit action now passes the chatbot's current value (the history)
    # to the `respond` function.
    msg.submit(respond, [msg, chatbot, role], [msg, chatbot])

    # The clear button now clears the chatbot and the message box.
    clear.click(lambda: ([], ""), None, [chatbot, msg], queue=False)

    gr.Markdown("Made with 💡 by Dave")

demo.launch()