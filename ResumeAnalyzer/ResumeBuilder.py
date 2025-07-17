import streamlit as st
import os
import requests
import pdfplumber

#import streamlit as st
st.title("✅ App is running!")


# --- API key ---
GROQ_API_KEY = " " # " copy your-groq-api-key"

# --- Groq LLM API call ---
def call_groq_llm(prompt: str, model="llama3-70b-8192"): #llama3-70b-8192 #llama3-8b-8192
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        
        if "choices" in data:
            return data['choices'][0]['message']['content']
        else:
            st.error("❌ Groq API response malformed — check your API key or quota.")
            st.json(data)  # Display raw response for debugging
            return "Error: Unexpected response format from Groq."
        
    except requests.exceptions.HTTPError as http_err:
        st.error(f"HTTP error: {http_err}")
        return "Error: HTTP issue occurred."

    except Exception as e:
        st.error(f"Unexpected error: {e}")
        return "Error: Something went wrong."


# --- Extract text from PDF ---
def extract_text_from_pdf(uploaded_file):
    with pdfplumber.open(uploaded_file) as pdf:
        text = "\n".join(page.extract_text() or '' for page in pdf.pages)
    return text

# --- Streamlit UI ---
st.title("🔍 AI Resume Analyzer")
st.markdown("Upload your **resume** and a **job description**, and the AI will give feedback and suggestions.")

resume_file = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])
job_description = st.text_area("Paste Job Description")

if resume_file and job_description:
    resume_text = extract_text_from_pdf(resume_file)

    with st.spinner("Analyzing Resume..."):
        prompt = f"""
You are a career advisor. Compare the following resume with the job description.
1. Highlight missing skills or mismatches.
2. Suggest 3-5 improvements in the resume.
3. Rewrite any weak bullet points.

=== RESUME ===
{resume_text}

=== JOB DESCRIPTION ===
{job_description}
"""
        feedback = call_groq_llm(prompt)
        st.subheader("📊 Resume Analysis Report")
        st.write(feedback)
