#from transformers import pipeline
from sql_executor import execute_sql_query
import os
import requests
from schema_formatter import format_schema


# --- API key ---
GROQ_API_KEY = "" #or "your-groq-api-key"
GROK_API_URL = "https://api.groq.com/openai/v1/chat/completions"

# --- Groq LLM API call ---
def generate_sql_with_grok(prompt):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama3-70b-8192",
        "messages": [
            {"role": "system", "content": "You are an expert SQL assistant."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3,
        "max_tokens": 150
    }

    response = requests.post(GROK_API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        data = response.json()
        sql_response = data["choices"][0]["message"]["content"]
        return sql_response.strip()
    else:
        raise Exception(f"API Error: {response.status_code} - {response.text}")


def load_prompt(user_input):
    schema_text = format_schema()
    prompt_text = f"""
                    You are a SQL expert. Use the schema below to write an executable SQL query.

                    IMPORTANT:
                    - Use column names exactly as provided
                    - Do NOT invent column names like 'id' or 'name'
                    - No explanation, markdown, or formatting — only the SQL
                    User Request: "{schema_text}"

                    SQL:
                    """
    return prompt_text

import re

def extract_sql_from_response(response_text):
    """
    Extracts the SQL code from a markdown-style response with backticks.
    """
    # Look for code block in triple backticks
    match = re.search(r"```sql\\n(.*?)```", response_text, re.DOTALL | re.IGNORECASE)
    if match:
        return match.group(1).strip()

    # Fallback: look for any line that starts with SELECT
    lines = response_text.splitlines()
    for line in lines:
        if line.strip().upper().startswith("SELECT"):
            return line.strip()

    raise ValueError("SQL query could not be extracted.")




    # with open("prompt_template.txt", "r") as file:
    #     template = file.read()
    # return template.format(input=user_input)

def main():

    while True:
        user_input = input("Enter your question: ")
        if user_input.lower() in {"exit", "quit"}:
            print("👋 Goodbye!")
            break

        

        try:
            prompt = load_prompt(user_input)
            sql_query = generate_sql_with_grok(prompt)
            print("raw qrok sql   \n",sql_query)
            #sql_query = extract_sql_from_response(sql_query)
            #print(f"\nGenerated SQL:\n{sql_query}")

            
            DB_PATH = os.path.join(os.path.dirname(__file__), "db.sqlite")
            print("db_path",DB_PATH)
            result = execute_sql_query(DB_PATH, sql_query)
            print("\nResult:")
            for row in result:
                print(row)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
