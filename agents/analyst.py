from autogen_agentchat.agents import AssistantAgent
from models.openrouter_client import get_llama_client

def get_analyst_agent():
    system_msg = """You are a Senior Data Analyst.
    Your job is to look at the output of the Data Engineer and provide insights.
    - Explain the trends or findings in simple terms.
    - If a chart was generated, mention it in your summary.
    - Do not write any code yourself.
    - Provide a final conclusion for the user.
    - You MUST end your response with the word 'TERMINATE'.""" # <-- The Kill Switch

    return AssistantAgent(
        name="Data_Analyst",
        model_client=get_llama_client(),
        system_message=system_msg
    )