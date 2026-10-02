from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

llm = HuggingFaceEndpoint(
    # repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    # repo_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    # repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)

model= ChatHuggingFace(llm=llm)


# this particular parsion api is not response
template1 = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=['topic']
)

template2 = PromptTemplate(
    template="Write a 5 line summary on the following text. \n {text}",
    input_variables=['text']
)

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

res = chain.invoke({'topic': 'black hole'})

print(res)
