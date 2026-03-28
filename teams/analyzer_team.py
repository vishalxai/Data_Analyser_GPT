from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination
from agents.engineer import get_engineer_agent
from agents.analyst import get_analyst_agent
from agents.code_executor_agent import getCodeExecutorAgent
from config.local_utils import get_local_executor 

def get_analyzer_team():
    # 1. Setup the Local Executor
    local_executor = get_local_executor()
    
    # 2. Setup the Team Members
    engineer = get_engineer_agent()
    analyst = get_analyst_agent()
    executor_agent = getCodeExecutorAgent(local_executor)
    
    # 3. Define when the meeting ends
    termination_condition = TextMentionTermination("TERMINATE")
    
    # 4. Create the Team
    team = RoundRobinGroupChat(
        [engineer, executor_agent, analyst],
        termination_condition=termination_condition
    )
    
    return team