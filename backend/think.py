# This file is responsible for all of D.A.N.T.E.'s thinking and processing.
# It contains different templates depending on which AI model you use and where you get it from. 
# Update your .env file to choose your model and, if applicable, your API key. 
# For purposes of efficiency, only needed libraries are imported. 

from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=Path("../.env"))

THINKING_MODEL_MODE = os.getenv("THINKING_MODEL_MODE")
if THINKING_MODEL_MODE is "OLLAMA_CLOUD":
    try:
        messages = [
            {"role": "system", "content": "You are D.A.N.T.E., a helpful and friendly AI assistant. You are capable of performing a variety of tasks, including answering questions, providing information, and assisting with various activities. You are designed to be user-friendly and provide accurate and helpful responses."},
            {"role": "system", "content": f"The user has provided the following personality preferences. Please follow them as best you can: {os.getenv('PERSONALITY_PREFERENCES')}"}
        ]
        import ollama
        OLLAMA_API_KEY = os.getenv("OLLAMA_API_KEY")
        OLLAMA_CLOUD_MODEL = str(os.getenv("OLLAMA_CLOUD_MODEL"))
        if OLLAMA_CLOUD_MODEL in ollama.list():
            pass
        else:
            ollama.pull(OLLAMA_CLOUD_MODEL)
        global getResponse
        def getResponse(prompt):
            client  = ollama.Client(
                host = 'https://ollama.com',
                headers = {'Authorization': f'Bearer {OLLAMA_API_KEY}'}
            )
            messages.append({
                "role": "user",
                "content": prompt
            })
            full_response = ""
            for part in client.chat(OLLAMA_CLOUD_MODEL, messages=messages, stream = True):
                yield part.message.content
                full_response += str(part.message.content)
                messages.append({
                    "role": "bot",
                    "content": full_response
                })
    except Exception as e:
        if isinstance(e, ImportError):
            raise RuntimeError("You need to install the Ollama python library. Open a terminal and run \"pip install ollama\".")
        else:
            raise RuntimeError(f"An unknown error occurred while setting up Ollama cloud: {e}")
    

