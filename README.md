# 📊 Autonomous AI Data Analyst

An end-to-end, multi-agent AI system that autonomously analyzes datasets, writes and executes Python code in a secure sandbox, and generates business insights with visual charts. 

**Live Demo:** [Link to your Hugging Face Space will go here]

![App Screenshot](temp/profit_analysis.png) *
## 🧠 System Architecture

This project moves beyond simple API calls by orchestrating a team of specialized AI agents using **Microsoft AutoGen**. 

1. **The Frontend (Streamlit):** Provides a clean, user-friendly interface for CSV uploads and natural language querying.
2. **The Brain (Llama 3.3 via OpenRouter):** Powers the reasoning and coding capabilities of the agents.
3. **The Data Engineer Agent:** Autonomously writes Pandas and Matplotlib code to manipulate data and generate visualizations based on the user's prompt.
4. **The Code Executor (Secure Sandbox):** Executes the Engineer's code in an isolated environment (`LocalCommandLineCodeExecutor` for cloud deployment, or a `Docker` container for local security), ensuring safe execution of LLM-generated scripts.
5. **The Data Analyst Agent:** Reviews the numerical and visual output from the Executor and synthesizes it into actionable, boardroom-ready business insights.

## 🚀 Features

* **Natural Language to Code:** Upload any CSV and ask questions in plain English.
* **Autonomous Execution:** The system writes the code, installs necessary dependencies, runs it, and debugs its own errors if they occur.
* **Dynamic Visualizations:** Generates and displays charts (bar, line, scatter) natively in the UI.
* **Containerized Deployment:** Fully packaged with a `Dockerfile` for seamless deployment to cloud environments like Hugging Face Spaces.

## 🛠️ Tech Stack

* **Orchestration:** Microsoft AutoGen (`autogen-agentchat`, `autogen-ext`)
* **LLM:** Llama 3.3 (Routed via OpenRouter)
* **UI Framework:** Streamlit
* **Data Science:** Pandas, Matplotlib, NumPy
* **Infrastructure:** Docker, Python 3.11

## 💻 Local Installation

To run this project locally on your machine:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/autonomous-ai-data-analyst.git](https://github.com/your-username/autonomous-ai-data-analyst.git)
   cd autonomous-ai-data-analyst

* Create a virtual environment:
   python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

* Install Dependencies:
pip install -r requirements.txt

* Set up Environment Variables:
Create a .env file in the root directory and add your API key:

* Run the Streamlit App:
export PYTHONPATH=.
streamlit run app.py

☁️ Cloud Deployment
Built by [vishal singh /https://www.linkedin.com/in/vishalxai/] as a demonstration of autonomous AI agent orchestration.