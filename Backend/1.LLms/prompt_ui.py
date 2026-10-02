import streamlit as st
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import os


load_dotenv()

model = ChatOpenAI(
    model=os.getenv("model"),
    api_key=os.getenv("api_key"),
    base_url=os.getenv("base_url")
    
)


# UI
st.header("This is header")
paper_input = st.selectbox("Select Research Paper name", ["Attention is all you Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"])

style_input = st.selectbox("Select Explaination Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"])

length_input = st.selectbox("Select Explaination Length", ["short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explaination)"])


template = PromptTemplate(
    template = """
Please summaries the research paper titled {paper_input} with the following specification:
Explain style: {style_input},
Explaination length: {length_input}

1. Mathematical details:
    - Include relevant mathematical equations if present in the paper.
    - Explain the mathematical concepts using simple, intutive code snippets where applicable
2. Analogies:
    - Use relatable analogies to simplify complex ideas.
If certain information is not available in the paper, respond with: "Insufficient Information available" instead of guessing.

Ensure the summary is clear, accurate and aligned with the provided style and length.

""",
input_variables=['paper_input', 'style_input', 'length_input']
)


# fill in the placeholder
prompt = template.invoke(
    {
        'paper_input':paper_input,
        'style_input': style_input,
        'length_input': length_input
    }
)



if st.button("Summaries"):
    result = model.invoke(prompt)
    st.write(result.content)