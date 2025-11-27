# 🎓 Mentora: Your Multi-Agent Study Navigator

> [cite_start]**"Not just a mentor - Your multi-agent study navigator."** [cite: 4]

[cite_start]Mentora is an AI-powered, modular learning companion designed to help students bridge the gap between static study materials and active, personalized learning[cite: 30, 31]. [cite_start]Built entirely on the low-code automation platform **n8n**, Mentora automates scheduling and transforms passive reading into an interactive experience[cite: 31, 32].

---

## 📖 Table of Contents
- [About the Project](#-about-the-project)
- [Key Features](#-key-features)
- [System Architecture](#-system-architecture)
- [Tech Stack](#-tech-stack)
- [Getting Started](#-getting-started)
- [Roadmap](#-roadmap)
- [Team](#-team)

---

## 🧐 About the Project

[cite_start]In the modern academic landscape, students often struggle with time management and maintaining consistency due to a lack of accountability[cite: 36]. [cite_start]Furthermore, reading complex technical PDFs often leads to passive consumption rather than deep understanding[cite: 37].

**Mentora** solves these problems by deploying intelligent agents that work cohesively to:
* **Automate Planning:** Remove the friction of manual scheduling.
* **Enhance Comprehension:** Turn static PDFs into interactive conversations.
* [cite_start]**Centralize Workflow:** Combine disparate tools into one cohesive ecosystem[cite: 32].

---

## ✨ Key Features (Currently Implemented)

We have currently deployed two core agents powered by **n8n** and **Groq LLM**:

### 1. 📅 Calendar & Task Scheduling Agent
[cite_start]This agent acts as your personal academic assistant, ensuring you never miss a deadline[cite: 47, 54].
* [cite_start]**Smart Integration:** Connects directly with **Google Calendar** and **Google Tasks**[cite: 50].
* [cite_start]**Automated Management:** Allows users to set deadlines and track upcoming study events automatically[cite: 48].
* [cite_start]**Time Zone Intelligence:** Detects user time zones for accurate scheduling[cite: 51].

### 2. 🤖 Interactive RAG Agent (PDF Analyzer)
[cite_start]Powered by Retrieval-Augmented Generation (RAG), this agent transforms how you interact with study materials[cite: 55].
* [cite_start]**Chat with Data:** Upload textbooks or research papers and ask questions directly[cite: 61].
* [cite_start]**Smart Summarization:** Instantly generate summaries of key concepts from dense text[cite: 60].
* [cite_start]**Active Recall:** Generates quizzes based on the content to test your knowledge[cite: 62].

---

## 🏗 System Architecture

[cite_start]The system utilizes an **Agent Router** to classify user inputs and direct them to the appropriate agent[cite: 86].


* [cite_start]**Input:** User Interface (Streamlit/Web App)[cite: 85].
* [cite_start]**Processing:** n8n workflows integrated with Groq LLM APIs[cite: 82].
* [cite_start]**Output:** Unified responses via the dashboard or Google Workspace updates[cite: 96].

---

## 🛠 Tech Stack

* [cite_start]**Core Automation:** [n8n](https://n8n.io/) (Node-based automation) [cite: 31]
* [cite_start]**LLM Inference:** [Groq API](https://groq.com/) (Fast AI inference) [cite: 82, 99]
* [cite_start]**Integrations:** Google Calendar API, Google Tasks API [cite: 50]
* [cite_start]**Frontend:** Streamlit [cite: 85]
* **Language:** Python / JavaScript (via n8n nodes)

---

## 🚀 Getting Started

### Prerequisites
* An **n8n** instance (self-hosted or cloud).
* **Groq API Key** for LLM processing.
* **Google Cloud Console** credentials (OAuth 2.0) for Calendar/Tasks integration.

### Installation

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/AmandeepS1ngh/Mentora.git](https://github.com/AmandeepS1ngh/Mentora.git)
    ```

2.  **Import Workflows**
    * Open your n8n dashboard.
    * Import the `.json` workflow files located in the `/workflows` directory of this repo.

3.  **Configure Credentials**
    * In n8n, set up credentials for "Google Calendar" and "Groq".
    * Update the environment variables in your `.env` file if running locally.

4.  **Run the Interface**
    ```bash
    streamlit run app.py
    ```

---

## 🛣 Roadmap

The following agents are designed and planned for future updates:

- [ ] [cite_start]**Personalized Study Plan Generator:** Adaptive planning that adjusts to missed tasks and learning pace[cite: 65, 70].
- [ ] [cite_start]**Voice-Based Reflection Tracker:** Uses Whisper API to transcribe and evaluate spoken self-explanations (Feynman Technique)[cite: 74, 75].
- [ ] [cite_start]**Dashboard Integration:** A unified view for progress tracking[cite: 96].

---

## 👥 Team

**Project By:**
* [cite_start]**Amandeep Singh** (2310993771) [cite: 7, 8]
* [cite_start]**Prachi Pahwa** (2310993904) [cite: 9, 10]

**Guided By:**
* **Dr. [cite_start]Harshvardhan** [cite: 17]

[cite_start]*Chitkara University Institute of Engineering & Technology* [cite: 18]
