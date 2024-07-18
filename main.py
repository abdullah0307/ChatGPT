import os
import openai
import streamlit as st
from dotenv import load_dotenv
from utils import get_completion_from_messages

# Yaha ma apna env variable load kar raha hun
load_dotenv()

# Yaha ma secret kay set kar raha hun
openai.api_key = os.environ["OPEN_AI_API_KEY"]

communication = [
    {
        "role": "assistant",
        "content": "you are a friendly chatbot and answer all the question of the \
        user but when the user say bye or goodbye you will response only bye always \
        output in well format way using escape sequences"
    }
]

while True:
    message = input("User:")
    communication.append({"role": "user", "content":message})
    bot_response = get_completion_from_messages(communication)
    print("bot:", bot_response)
    communication.append({"role": "assistant", "content":bot_response})
    if "bye" in bot_response.lower():
        break




