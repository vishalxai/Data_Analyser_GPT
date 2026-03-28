import asyncio
from teams.analyzer_team import get_analyzer_team
from config.docker_utils import start_docker_container, stop_docker_container

async def main():
    team, docker_engine = get_analyzer_team()
    
    try:
        await start_docker_container(docker_engine)
        
        user_query = """
        Read the dataset 'superstore_data.csv' (it is located in your current directory). 
        I need you to act as a Business Intelligence Analyst.
        1. Calculate the total 'Sales' for each 'Region'.
        2. Plot a bar chart showing the total sales by region. Make it look professional with a title and labels.
        3. Save the chart directly to the current directory as 'regional_sales.png'.
        """
        
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