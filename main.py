import asyncio
from teams.analyzer_team import get_analyzer_team
from config.docker_utils import start_docker_container, stop_docker_container

async def main():
    team, docker_engine = get_analyzer_team()
    
    try:
        await start_docker_container(docker_engine)
        
        user_query = "Create a pandas dataframe with 5 rows of random sales data and plot a line chart."
        print(f"\n🚀 Starting Task: {user_query}\n")
        
        # Watch the conversation in real-time!
        async for msg in team.run_stream(task=user_query):
            # This safety check prevents the TaskResult error
            if hasattr(msg, 'source'):
                print(f"--- {msg.source} ---\n{msg.content}\n")
            
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        await stop_docker_container(docker_engine)

if __name__ == "__main__":
    asyncio.run(main())