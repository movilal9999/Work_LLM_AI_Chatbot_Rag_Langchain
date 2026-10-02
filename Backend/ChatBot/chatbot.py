from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage 
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatOpenAI(
    api_key = os.getenv("api_key"),
    model = os.getenv("model"),
    base_url=os.getenv("base_url")
)
chatHistory = [
    SystemMessage(content="you are a helpful assistance")
]
prompt = input("You :")

while True:

    if prompt == "exit":
        break;

    chatHistory.append(HumanMessage(content=prompt))
    result = model.invoke(prompt)
    print("AI :",result.content)
   
    chatHistory.append(AIMessage(content = result.content))
    prompt = input("\n>> You :")

print(chatHistory)