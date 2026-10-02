from langchain_openai import OpenAIEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

from dotenv import load_dotenv
import os

load_dotenv()
documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'good player', holds many bating records.",
    "Rohit Sharma is known for his elegant batting and rcord-breaking double centuries",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query="tell me about the Virat Kohli"


embeddings = OpenAIEmbeddings(
    model=os.getenv("multi_model"),
    # Emb_model="nvidia/nemotron-3-embed-1b:free",
    base_url=os.getenv("base_url"),
    api_key=os.getenv("api_key"),  # Your OpenRouter key
    check_embedding_ctx_length=False)


query_embedding = embeddings.embed_query(query)
docs = embeddings.embed_documents(documents)

scores = cosine_similarity([query_embedding], docs)[0]

index, score = sorted(list(enumerate(scores)), key=lambda x: x[1])[-1]

print(query)
print(documents[index])
print("similarity score is :", score)
