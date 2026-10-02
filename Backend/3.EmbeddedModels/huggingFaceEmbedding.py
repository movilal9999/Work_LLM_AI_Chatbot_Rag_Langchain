
# from langchain_huggingface import HuggingFaceEmbeddings

# embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# text = "Delhi is the capital of india"

# vector = embedding.embed_query(text)

# print(str(vector))
# print(len(vector))

####  Multi Documentation

from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

documents = [
    "Delhi is the capital of india",
    "Up is my home city",
    "Ujjain is the city where i did my graduation"
    ]

vector = embedding.embed_documents(documents)

print(str(vector))
print(len(vector))
