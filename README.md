---
title: Autonomous Data Analyst
emoji: 📊
colorFrom: blue
colorTo: indigo
sdk: docker
pinned: false
---

# 📊 Autonomous AI Data Analyst

An end-to-end, multi-agent AI system that autonomously analyzes datasets, writes and executes Python code in a secure sandbox, and generates business insights with visual charts.

**🚀 Live Demo:** [Try it on Hugging Face Spaces](https://huggingface.co/spaces/vishalxai/Autonomous-Data-Analyst)

![App Screenshot](temp/profit_analysis.png)

## 🧠 System Architecture

This project moves beyond simple API calls by orchestrating a team of specialized AI agents using **Microsoft AutoGen**.

1. **The Frontend (Streamlit):** Clean interface for CSV uploads and natural-language querying.
2. **The Brain (Llama 3.3 via OpenRouter):** Powers the reasoning and coding capabilities of the agents.
3. **The Data Engineer Agent:** Autonomously writes Pandas and Matplotlib code to manipulate data and generate visualizations from the user's prompt.
4. **The Code Executor (Secure Sandbox):** Runs the Engineer's code in an isolated environment (`LocalCommandLineCodeExecutor` for cloud deployment, or a Docker container for local security), ensuring safe execution of LLM-generated scripts.
5. **The Data Analyst Agent:** Reviews the numerical and visual output and synthesizes it into actionable business insights.

## 🚀 Features

- **Natural language to code:** Upload any CSV and ask questions in plain English.
- **Autonomous execution:** The system writes the code, runs it, and debugs its own errors when they occur.
- **Dynamic visualizations:** Generates and displays charts (bar, line, scatter) natively in the UI.
- **Containerized deployment:** Packaged with a `Dockerfile` for deployment to Hugging Face Spaces.

## 🛠️ Tech Stack

- **Orchestration:** Microsoft AutoGen (`autogen-agentchat`, `autogen-ext`)
- **LLM:** Llama 3.3 (via OpenRouter)
- **UI:** Streamlit
- **Data science:** Pandas, Matplotlib, NumPy
- **Infrastructure:** Docker, Python 3.11

## 💻 Local Installation

```bash
# Clone the repository
git clone https://github.com/vishalxai/Data_Analyser_GPT.git
cd Data_Analyser_GPT

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables: create a .env file with your OpenRouter API key

# Run the app
export PYTHONPATH=.
streamlit run app.py
```

---

Built by [Vishal Singh](https://www.linkedin.com/in/vishalxai/) as a demonstration of autonomous AI agent orchestration.
