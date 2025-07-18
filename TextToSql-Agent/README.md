# 🧠 Text-to-SQL Agent (Grok + SQLite + Schema-Aware)

This project is an intelligent AI agent that converts **natural language questions into SQL queries** using a schema-aware approach. It supports:
- 🗃️ Multiple tables
- 📉 Poorly-named columns
- 📘 Column descriptions to guide the model
- 🧠 LLM-powered SQL generation via Grok API
- 🔁 Interactive loop: ask multiple questions until you type `exit`

---

## 🔧 Project Structure

text2sql-agent/
├── agent.py # Main loop: LLM + query executor
├── db.sqlite # SQLite database with sample data
├── schema_description.json # Table and column descriptions
├── schema_formatter.py # Formats schema for LLM prompt
├── sql_executor.py # Executes generated SQL safely
├── requirements.txt
└── README.md


---

## 🧪 Example Queries

Ask plain English questions like:
- `"Show all customer names who placed orders above ₹10,000"`
- `"Which customer spent the most?"`
- `"List total revenue per customer"`
- `"Show orders placed in July 2024"`

---

## 🛠️ Setup Instructions

1. **Clone the repo** or unzip the folder.
2. Make sure you have Python 3.8+ installed.
3. Install dependencies:

```bash
pip install -r requirements.txt

**## API key**
export GROK_API_KEY=your_grok_api_key_here

**##  Run the app**
python agent.py
