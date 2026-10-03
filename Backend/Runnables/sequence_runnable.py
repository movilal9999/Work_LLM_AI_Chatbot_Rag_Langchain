from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatOpenAI(
    api_key=os.getenv("api_key"),
    base_url=os.getenv("base_url"),
    model=os.getenv("model")
)

parser = StrOutputParser()

prompt = PromptTemplate(
    template="write a joke on the topic \n {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="Explain the following text \n {text}",
    input_variables=['text']
)

chain = RunnableSequence(prompt, model, parser, prompt2, model, parser)
result =chain.invoke({'topic':'cricket'})
print(result)

