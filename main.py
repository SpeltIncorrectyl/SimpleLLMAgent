from chat_model import ChatGPT
from agent import Agent
import tools
from chatbot import Chatbot

with open("openai_api_key.txt") as openai_api_key_file:
    openai_api_key = openai_api_key_file.read()

chatgpt4 = ChatGPT(openai_api_key, "gpt-4")
chatgpt = ChatGPT(openai_api_key, "gpt-3.5-turbo")

chatbot = Chatbot(chatgpt, "You are a helpful assistant, who can use a suite of tools to solve your user's problems.")
search_tool = tools.Search()
agent = Agent(chatbot, [search_tool])

agent.do("Who won the football today?")