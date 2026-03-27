# agents/code_executor_agent.py
from autogen_agentchat.agents import CodeExecutorAgent

def getCodeExecutorAgent(docker_executor):
    return CodeExecutorAgent(
        name='CodeExecutor',
        code_executor=docker_executor
    )