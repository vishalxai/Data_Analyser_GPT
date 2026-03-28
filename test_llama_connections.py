import asyncio
from models.openrouter_client import get_llama_client
# Correct import location for AutoGen 0.4 core messages
from autogen_core.models import UserMessage 

async def test_llm():
    print("🧠 Contacting Llama 3.3 via OpenRouter...")
    client = get_llama_client()
    
    try:
        # We pass a list containing a UserMessage object
        response = await client.create([
            UserMessage(content="Hello! Can you hear me? Respond with 'Bengaluru is ready for AI' if you are working.", source="user")
        ])
        
        print("\n--- LLM RESPONSE ---")
        print(response.content)
    except Exception as e:
        print(f"❌ Connection failed: {e}")

if __name__ == "__main__":
    asyncio.run(test_llm())