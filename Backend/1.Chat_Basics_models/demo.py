from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
import os

load_dotenv()


api_key=os.getenv('api_key')
model=os.getenv('model')
base_url=os.getenv('base_url')

llm = ChatOpenAI(
    api_key=api_key,
    base_url=base_url,
    model=model,
    temperature=0.2,
    max_completion_tokens=20
    )

res = llm.invoke("what is the capital of India")
print(res.content)
