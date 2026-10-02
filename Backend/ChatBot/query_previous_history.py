from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

# chat template
chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human', '{query}')
])


chat_history = []
# load_history
with open(r"C:\Users\movil\Desktop\LangChain_model\Backend\ChatBot\chat_history.txt") as f:
    chat_history.extend(f.readlines())


# create prompt
prompt = chat_template.invoke(
    {
        "chat_history":chat_history,
        "query": "where is my order"
    }
)
# chat_history.append(prompt)
# print(prompt)
print(chat_history)