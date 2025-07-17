# 🧠 Resume Analyzer – Agentic AI with Groq

This is a Streamlit app that analyzes your resume against a job description using a free LLM from Groq (e.g. LLaMA3). It gives intelligent, personalized suggestions to improve your resume.

## 🔍 Features

- Upload Resume (PDF/TXT)
- Upload Job Description
- LLM analyzes and gives bullet-point feedback
- Uses Groq's blazing-fast open-source LLMs

## 🏗 Architecture

![architecture diagram](assets/architecture.png)

## ⚙️ Tech Stack

- Python
- Streamlit
- Groq API (LLaMA3 / Gemma)
- dotenv

## 🚀 Getting Started

```bash
# 1. Clone this repo
git clone https://github.com/yourusername/resume-analyzer-agentic-ai
cd resume-analyzer-agentic-ai

# 2. Install dependencies
pip install -r requirements.txt

# 3. Add your Groq API key
cp .env.example .env
# Edit .env and add: GROQ_API_KEY=your_key_here

# 4. Run the app
streamlit run resumebuilder.py
