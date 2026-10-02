from langchain_openai import OpenAIEmbeddings

from dotenv import load_dotenv
import os

load_dotenv()

embeddings = OpenAIEmbeddings(
    base_url=os.getenv("base_url"),
    model=os.getenv("multi_model"),
    api_key=os.getenv("api_key"),
    check_embedding_ctx_length=False
)
documents = [
    "documents1", "documents2", "documents"
]
vector = embeddings.embed_documents(documents)

print(vector)
print(len(vector))