from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination
from agents.engineer import get_engineer_agent
from agents.analyst import get_analyst_agent
from agents.code_executor_agent import getCodeExecutorAgent
from config.docker_utils import getDockerCommandLineExecutor

def get_analyzer_team():
    # 1. Setup the "Body" (Docker)
    docker_executor = getDockerCommandLineExecutor()
    
    # 2. Setup the "Team Members"
    engineer = get_engineer_agent()
    analyst = get_analyst_agent()
    executor_agent = getCodeExecutorAgent(docker_executor)
    
    # 3. Define when the meeting ends (When someone says 'TERMINATE')
    termination_condition = TextMentionTermination("TERMINATE")
    
    # 4. Create the Team
    team = RoundRobinGroupChat(
        [engineer, executor_agent, analyst],
        termination_condition=termination_condition
    )
    
    return team, docker_executor