from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import Field, BaseModel
import os


load_dotenv()

model = ChatOpenAI(
    api_key=os.getenv("api_key"),
    base_url=os.getenv("base_url"),
    model=os.getenv("model")
)



class Facts(BaseModel):
    fact_1: str = Field(description="fact 1 about the topic")
    fact_2: str = Field(description="fact 2 about the topic")
    fact_3: str = Field(description="fact 3 about the topic")
    fact_4: str = Field(description="fact 4 about the topic")
    fact_5: str = Field(description="fact 5 about the topic")
    

parser = PydanticOutputParser(pydantic_object=Facts)

prompt = PromptTemplate(
    template="generate 5 fact about the {topic} \n {format_instruction}",
    input_variables=['topic'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

chain = prompt | model | parser

res = chain.invoke({'topic':'cricket'})

# print(res)
# print(type(res))
# print(res.model_dump())
# print(type(res.model_dump()))
# print(type(res))

# chain visualize

chain.get_graph().print_ascii()