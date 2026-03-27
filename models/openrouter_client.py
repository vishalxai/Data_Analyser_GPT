import os
from dotenv import load_dotenv
from autogen_ext.models.openai import OpenAIChatCompletionClient

load_dotenv()

def get_llama_client():
    """
    Returns the OpenRouter client configured for Llama 3.3 70B.
    """
    return OpenAIChatCompletionClient(
        model="meta-llama/llama-3.3-70b-instruct",
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPENROUTER_API_KEY"),
        model_info={
            "vision": False,
            "function_calling": True,
            "json_output": True,
            "family": "llama"
        }
    )