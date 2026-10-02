from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import JsonOutputParser
load_dotenv()

llm = HuggingFaceEndpoint(
    # repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    # repo_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    # repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)

model= ChatHuggingFace(llm=llm)


#  // new step 
parser = JsonOutputParser()
template = PromptTemplate(
    template="give me the name, city and age of a fictional person \n {format_instruction}",
    input_variables=[],
    partial_variables={'format_instruction':parser.get_format_instructions()}

)
prompt = template.format()
res = model.invoke(prompt)

final_res = parser.parse(res.content)
print(final_res)
print(type(final_res))