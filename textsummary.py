
import gradio as gr
import requests
import time
import os

API_URL = "https://router.huggingface.co/hf-inference/models/sshleifer/distilbart-cnn-6-6"
headers = {"Authorization":  f"Bearer {os.getenv('HF_TOKEN')}"}  # use your new token


def summarize(text):
    # Handle empty input
    if not text.strip():
        return "Please enter some text."

    # Handle short text
    if len(text.split()) < 20:
        return "Text too short to summarize."

    # Retry logic
    for _ in range(5):
        response = requests.post(
            API_URL,
            headers=headers,
            json={
                "inputs": text,
                "parameters": {
                    "max_length": 60,
                    "min_length": 20,
                    "do_sample": False,
                    "no_repeat_ngram_size": 3
                }
            }
        )

        data = response.json()

        if isinstance(data, list):
            return data[0]["summary_text"]
        else:
            time.sleep(2)

    return "Error: Could not generate summary."


#  Gradio UI
interface = gr.Interface(

    fn=summarize,
    inputs=gr.Textbox(lines=10, placeholder="Enter your text here..."),
    outputs=gr.Textbox(label="Summary"),
    title="Text Summarizer",
    description="Enter a long paragraph and get a summarized version using AI."
)

interface.launch(share=True)
