from autogen_agentchat.agents import AssistantAgent
from models.openrouter_client import get_llama_client

def get_engineer_agent():
    system_msg = """You are a Senior Data Engineer. 
    Your only job is to write code to solve data tasks.
    - FIRST, output a ```bash code block to install any needed libraries (e.g., pip install pandas matplotlib).
    - THEN, output your ```python code block to solve the task.
    - Save any charts or files DIRECTLY to the current directory (e.g., use `plt.savefig('chart.png')`). Do NOT use 'temp/' in your file paths!
    - NEVER use the word 'TERMINATE'. Wait for the executor to run your code."""

    return AssistantAgent(
        name="Data_Engineer",
        model_client=get_llama_client(),
        system_message=system_msg
    )