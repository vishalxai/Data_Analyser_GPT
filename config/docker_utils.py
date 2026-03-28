# utils/docker_utils.py
from autogen_ext.code_executors.docker import DockerCommandLineCodeExecutor
from .constants import TIMEOUT_DOCKER, WORK_DIR_DOCKER

def getDockerCommandLineExecutor():
    # Builds the Docker object using our constants
    return DockerCommandLineCodeExecutor(
        image="python:3-slim",
        work_dir=WORK_DIR_DOCKER,
        timeout=TIMEOUT_DOCKER
    )

async def start_docker_container(docker):
    await docker.start()
    print("🚀 Docker Sandbox Started")

async def stop_docker_container(docker):
    await docker.stop()
    print("🛑 Docker Sandbox Stopped")