from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ('system','you are a {domain} expert'),
    ('human','tell me about the {topic}')

])

prompt = chat_template.invoke({'domain':'cricket', 'topic':'Dusra'})
print(prompt)