from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
load_dotenv()
import os

# llm = HuggingFaceEndpoint(
#     # repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
#     # repo_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
#     repo_id="meta-llama/Llama-3.1-8B-Instruct",
#     # repo_id="meta-llama/Llama-3.1-8B-Instruct",
#     task="text-generation"
# )

# model= ChatHuggingFace(llm=llm)

model = ChatOpenAI(
    api_key=os.getenv("api_key"),
    base_url=os.getenv("base_url"),
    model=os.getenv("model")
    
)


# this particular parsion api is not response
template1 = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=['topic']
)

template2 = PromptTemplate(
    template="""
Write a 5 line summary on the following text. {text}

""",
    input_variables=['text']
)

prmpt1 = template1.invoke({'topic': 'black hole'})
res1 = model.invoke(prmpt1)

prompt2 = template2.invoke({'text':res1.content})

res2 = model.invoke(prompt2)
print(res2.content)



# res = model.invoke("what is the capital of india")
# print(res.content)
