from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
# from langchain.output_parsers import StructureOutputParser, ResponseSchema
from pydantic import BaseModel, Field
load_dotenv()

llm = HuggingFaceEndpoint(
    # repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    # repo_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    # repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)

model= ChatHuggingFace(llm=llm)

# schema = [
#     ResponseSchema(name='fact_1', description='fact 1 about the topic'),
#     ResponseSchema(name='fact_2', description='fact 2 about the topic'),
#     ResponseSchema(name='fact_3', description='fact 3 about the topic')
# ]

class Facts(BaseModel):
    Fact_1: str = Field(description="fact 1 about the topic")
    Fact_2: str = Field(description="fact 2 about the topic")
    Fact_3: str = Field(description="fact 3 about the topic")



# parser = StructureOutputParser.from_response_schema(schema) ### this is depricated
parser = PydanticOutputParser(pydantic_object=Facts)

template = PromptTemplate(
    template='Give 3 fact about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction':parser.get_format_instructions()}

)

chain = template | model | parser

res = chain.invoke({'topic':'black hole'}) 
# print(res)  ## object not dictionary
print(res.model_dump())

