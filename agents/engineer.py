from autogen_agentchat.agents import AssistantAgent
from models.openrouter_client import get_llama_client

def get_engineer_agent():
    return AssistantAgent(
        name="Data_Engineer",
        model_client=get_llama_client(),
        system_message="""You are a Senior Data Engineer. 
        Your task is to write Python code using pandas and matplotlib to analyze data.
        - Always use 'temp/' as the directory for any files or plots.
        - If a chart is requested, save it as 'temp/chart.png'.
        - Output ONLY the code block.
        - When the task is complete, end your message with 'TERMINATE'."""
    )