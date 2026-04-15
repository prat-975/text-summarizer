# AI Text Summarizer

An AI-powered web application that summarizes long text into concise and meaningful summaries using Hugging Face Transformers and Gradio.

---

## Features

* Summarizes long paragraphs into short, clear summaries
* Handles empty and short inputs gracefully
* Interactive and user-friendly UI using Gradio
* Uses a pre-trained NLP model (DistilBART)
* Secure API usage with environment variables

---

## Tech Stack

* Python
* Gradio
* Hugging Face Transformers
* Requests API
* Python-dotenv

---

## How It Works

1. User enters a long text input
2. The app sends the text to a Hugging Face model
3. The model processes and generates a summary
4. The summarized text is displayed instantly

---

## Project Structure

text-summarization/
│
├── app.py
├── textsummary.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env (not pushed to GitHub)

---

## Run Locally

### 1. Clone the repository

git clone https://github.com/prat-975/text-summarizer.git
cd text-summarizer

### 2. Install dependencies

pip install -r requirements.txt

### 3. Add environment variable

Create a `.env` file in the root directory and add:

HF_TOKEN=your_huggingface_token

### 4. Run the app

python app.py

---

## Live Demo

(Add your Hugging Face Space link here once deployed)

---

## Example

### Input

Artificial Intelligence is transforming industries by improving efficiency and enabling new innovations across sectors.

### Output

AI is transforming industries by improving efficiency and enabling innovation.

---

## Future Improvements

* Add support for multiple languages
* Improve summary quality using larger models
* Add file upload (PDF/Text summarization)
* Deploy using Docker and Kubernetes
* Add authentication and user history

---

## Security Note

Sensitive data like API tokens are stored using environment variables and are not exposed in the codebase.

---

## Learning Source

This project was built as part of learning from Genailearniverse.
