### My Work
# Generative AI 

# multiples projects in this single repo related all Gen AI


# 2. Create a virtual environment
python -m venv .venv

> Windows
.venv\Scripts\activate

> macOS / Linux
source .venv/bin/activate

# . Configure environment variables
cd LangChain_model/Backend
copy .env.example .env       # Windows
cp .env.example .env         # macOS/Linux

 # .env
 api_key=your_actual_api_key
base_url=https://your-endpoint-url/v1
model=your_model_name
HUGGINGFACEHUB_API_TOKEN=hf_xxxxxxxxxxxxxxxx


# 4. Install dependencies
cd LangChain_model/Backend
pip install -r requirements.txt

cd ../../Chatbots_projects/Email_Rewriter_Tool
pip install -r requirements.txt

cd ../Product_Description_Generator
pip install -r requirements.txt

cd ../Sentiment_Analyzer_API
pip install -r requirements.txt

 # Running the Projects
LangChain_model 
     Core Demos
cd LangChain_model/Backend

> LLMs
python 1.LLMs/demo.py
python 1.LLMs/prompt_ui.py
python 1.LLMs/prompts2.py

> Chat Models
python 2.ChatModels/chat_model_hf_api.py

> Embeddings
python 3.EmbeddedModels/Embedding.py
python 3.EmbeddedModels/Documents_similarity.py
python 3.EmbeddedModels/huggingFaceEmbedding.py
python 3.EmbeddedModels/multiEmbedding.py

> Chains
python Chains/simple_chain.py
python Chains/sequential_chain.py
python Chains/parallel_chains.py
python Chains/conditional_chain.py

> ChatBot
python ChatBot/chatbot.py

> Output Parsers
python OutputParser/main.py
python OutputParser/JsonFormate.py
python OutputParser/PydanticOutputParser.py

# LangChain_model FastAPI Chatbot

cd LangChain_model/Backend/model
uvicorn main:app --reload

Open http://127.0.0.1:8000/docs

# Chatbot Projects (FastAPI each)

> Email Rewriter Tool
cd Chatbots_projects/Email_Rewriter_Tool
uvicorn main:app --reload --port 8001

> Product Description Generator
cd ../Product_Description_Generator
uvicorn main:app --reload --port 8002

> Sentiment Analyzer API
cd ../Sentiment_Analyzer_API
uvicorn main:app --reload --port 8003

#  FILE 4 ->  LangChain_model/Backend/requirements.txt
Full path: FREE_LANCING_CONTENT/LangChain_model/Backend/requirements.txt

langchain
langchain-core
langchain-community
langchain-openai
langchain-huggingface
huggingface_hub
pydantic
python-dotenv
fastapi
uvicorn[standard]
streamlit
sentence-transformers
numpy
requests
httpx
