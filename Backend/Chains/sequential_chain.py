from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
import os
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(
    api_key=os.getenv("api_key"),
    base_url=os.getenv("base_url"),
    model=os.getenv("model")
)

parser = StrOutputParser()

template1 = PromptTemplate(
    template="generate the report base on the fact of {topic} with actual report",
    input_variables=['topic']
)

template2 = PromptTemplate(
    template="summaries the given text in 5 lines {text}",
    input_variables=['text']
)


chain = template1 | model | parser | template2 | model | parser
res = chain.invoke({'topic': "Future of freelancing tech skill on topic  rag based chatbot"})
print(res)
# print(type(res))
chain.get_graph().print_ascii()