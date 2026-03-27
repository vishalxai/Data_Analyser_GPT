import asyncio
from autogen_agentchat.messages import TextMessage
from autogen_core import CancellationToken

# These match your folder structure
from config.docker_utils import getDockerCommandLineExecutor, start_docker_container, stop_docker_container
from agents.code_executor_agent import getCodeExecutorAgent

async def main():
    # 1. Setup the Docker engine
    docker_executor = getDockerCommandLineExecutor()
    
    # 2. Setup the Agent
    agent = getCodeExecutorAgent(docker_executor)
    
    # 3. Start Docker
    await start_docker_container(docker_executor)
    
    # 4. Define a simple test task
    message = TextMessage(
        content="Please run: \n```python\nprint('Docker is working for Vishal!')\n```",
        source="user"
    )
    
    try:
        print("⏳ Running code inside Docker...")
        # The agent processes the message and runs the code block
        response = await agent.on_messages([message], CancellationToken())
        
        print("\n--- AGENT RESPONSE ---")
        print(response.chat_message.content)
        
    except Exception as e:
        print(f"❌ Error during execution: {e}")
        
    finally:
        # 5. ALWAYS stop Docker to save Mac resources
        await stop_docker_container(docker_executor)

if __name__ == "__main__":
    asyncio.run(main())