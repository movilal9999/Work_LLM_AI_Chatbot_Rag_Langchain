from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
from pydantic import BaseModel
from typing import Literal
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatOpenAI(
    api_key=os.getenv("api_key"),
    base_url=os.getenv("base_url"),
    model=os.getenv("model")
)

class Feedback(BaseModel):
    Sentiment: Literal['positive', 'negative']


parser2 = PydanticOutputParser(pydantic_object=Feedback)


template1 = PromptTemplate(
    template="generate the Sentiment of the following feedback text into positive or negative \n {feedback} \n {format_instruction}",
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser2.get_format_instructions()}
)

parser = StrOutputParser()

prompt2 = PromptTemplate(
    template="Write an appropriate response to this positive feedback \n {feedback}",
    input_variables=['feedback']
)
prompt3 = PromptTemplate(
    template="write an appropriate response to this negative feedback \n {feedback}",
    input_variables=['feedback']
)

classification_chain = template1 | model | parser2

branch_chain = RunnableBranch(
    (lambda x: x.Sentiment == 'positive', prompt2 | model | parser),
    (lambda x: x.Sentiment == 'negative', prompt3 | model | parser),
    (lambda x : "could not find Sentiment")
)

chain = classification_chain | branch_chain

res = chain.invoke({'feedback':"your product is not and service also bad features"})

print(res)

# res = classification_chain.invoke({'feedback': 'Features of the product is best'})
# print(res.Sentiment)

chain.get_graph().print_ascii()