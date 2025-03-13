import gradio as gr
from utils.openai_client import OpenAIClient

def chat_with_openai(user_input, api_key):
    openai_client.set_api_key(api_key)
    response = openai_client.get_response(user_input)
    return response

openai_client = OpenAIClient()

iface = gr.Interface(
    fn=chat_with_openai,
    inputs=[
        gr.Textbox(label="Enter your message"),
        gr.Textbox(label="Enter your OpenAI API Key", type="password")
    ],
    outputs=gr.Textbox(label="Response from OpenAI"),
    title="OpenAI Chat",
    description="Chat with OpenAI using your API key."
)

if __name__ == "__main__":
    iface.launch()
