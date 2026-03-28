# config/local_utils.py
from autogen_ext.code_executors.local import LocalCommandLineCodeExecutor
import os

def get_local_executor():
    # Ensure the temp directory exists
    os.makedirs("temp", exist_ok=True)
    
    # This runs code directly on your machine inside the temp folder
    return LocalCommandLineCodeExecutor(
        work_dir="temp",
        timeout=120
    )