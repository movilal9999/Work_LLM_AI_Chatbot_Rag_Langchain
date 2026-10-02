from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

# Using OpenAIEmbeddings class but pointing to OpenRouter
embeddings = OpenAIEmbeddings(
    # model="nvidia/nemotron-3-embed-1b:free",  # Free model from OpenRouter
    model=os.getenv("emb_model"),
    # Emb_model="nvidia/nemotron-3-embed-1b:free",
    base_url=os.getenv("base_url"),
    api_key=os.getenv("api_key"),  # Your OpenRouter key
    check_embedding_ctx_length=False
)

# Embed a single query
vector = embeddings.embed_query("Delhi is the capital of India")

print(str(vector))
print(len(vector))
