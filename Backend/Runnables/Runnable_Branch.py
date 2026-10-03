from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableBranch
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
    template="write a report on the topic \n {topic}",
    input_variables=['topic']
)

promtp2 = PromptTemplate(
    template="Summaries the text \n {text}",
    input_variables=['text']
)
report_gen_chain = RunnableSequence(prompt, model, parser)

branch_chain = RunnableBranch(
    (lambda x : len(x.split()) > 500, RunnableSequence(promtp2, model, parser)),
    RunnablePassthrough()
)

final_chain = RunnableSequence(report_gen_chain, branch_chain)
res = final_chain.invoke({'topic': "Gen AI Future"})
print(res)
final_chain.get_graph().print_ascii()

