# 🎓 Mentora – Your Smart Study Assistant

Mentora is an AI-powered learning companion built on **n8n** that helps students stay consistent, understand study material better, and avoid procrastination. It turns normal studying into an interactive and well-organized experience.

---

## 📌 What is Mentora?

Students often struggle with:
- Time management
- Forgetting important deadlines
- Reading complex PDFs without understanding

Mentora solves these problems using automation and intelligent agents.  
It helps you:
- Schedule tasks and study reminders automatically
- Convert PDF textbooks into an interactive chat experience
- Stay accountable and consistent in learning

---

## ✨ Current Features

### 1️⃣ Calendar & Task Scheduling Agent
- Connects with **Google Calendar** and **Google Tasks**
- Automatically adds and tracks study deadlines
- Detects user’s time zone for accurate scheduling

### 2️⃣ Interactive PDF Learning Agent (RAG)
- Upload textbooks or PDFs and **chat with the content**
- Generate instant summaries of technical topics
- Practice retention using automatically generated quizzes (active recall)

---

## 🧠 System Overview

Mentora uses an **Agent Router** that classifies user queries and directs them to the appropriate agent.

- Workflows are built and automated in **n8n**
- Language understanding and reasoning powered by **Groq LLM**
- Outputs are displayed in a **Streamlit dashboard** or synced with Google Workspace

---

## 🧰 Tech Stack

| Component | Technology |
|----------|-------------|
| Automation | n8n |
| LLM | Gemini 2.0 |
| Integrations | Google Calendar API, Google Tasks API |
| Frontend | Streamlit |
| Languages | Python, JavaScript |

---

## 🚀 Getting Started

### Prerequisites
- n8n instance (self-hosted or cloud)
- Groq API Key
- Google Calendar & Google Tasks OAuth Credentials

### Installation

1. Clone this repository:
   git clone https://github.com/AmandeepS1ngh/Mentora.git

Import n8n workflows:

2.Open the n8n dashboard

Import all .json workflow files from the /workflows folder

3.Configure credentials in n8n:

Google Calendar

Google API

Start the user interface:
streamlit run app.py

   
