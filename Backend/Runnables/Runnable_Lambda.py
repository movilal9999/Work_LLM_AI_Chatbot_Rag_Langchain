# generate the joke and a function that count the length of all characters

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda

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

joke_gen_chain = RunnableSequence(prompt, model, parser)
def count_word(joke_gen_chain):
    cnt = 0
    for word in joke_gen_chain.split():
        cnt += 1
    # return len(joke_gen_chain)
    return cnt

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'count': RunnableLambda(count_word)
})

chain = RunnableSequence(joke_gen_chain, parallel_chain)
res = chain.invoke({'topic':'cricket'})
print(res)

# chain.get_graph().print_ascii()
