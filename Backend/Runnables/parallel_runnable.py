from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatOpenAI(
    api_key=os.getenv("api_key"),
    base_url=os.getenv("base_url"),
    model=os.getenv("model")
)

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template="generate all the pros of the freelacing skill \n {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template = "generate all the cons of the freelancing skill \n {topic}",
    input_variables=['topic']
)

prompt3 = PromptTemplate(
    template="Merge the pros and cons",
    input_variables=[]
)

parallel_chain = RunnableParallel({
     'pros': RunnableSequence(prompt1, model, parser),
     'cons': RunnableSequence(prompt2, model, parser)
})

res = parallel_chain.invoke({'topic':'Rag based chatbot'})
print(res['pros'])
print("\n hii")
print(res['cons'])
