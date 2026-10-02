from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.runnables import RunnableParallel
from dotenv import load_dotenv

import os
load_dotenv()


# OpenRouter
model1 = ChatOpenAI(
    api_key=os.getenv("api_key"),
    base_url=os.getenv("base_url"),
    model=os.getenv('model')

)

# Gemini
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task='text-generation'
)
model2 = ChatHuggingFace(llm=llm)

# model2 = ChatOpenAI(
#     api_key=os.getenv("api_keyg"),
#     base_url=os.getenv("base_urlg"),
#     model=os.getenv('modelg')

# )

prompt1 = PromptTemplate(
    template="Generate short and simple notes from the following text \n {text}",
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template="Generate 5 short Questions and answers from the following text \n {text}",
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template="Merge the provided notes and quiz into a single documents \n quiz -> {quiz} and notes -> {notes}",
    input_variables=['quiz', 'notes']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz': prompt2 | model2 | parser
})

merge_chain = prompt3 | model2 | parser

chain = parallel_chain | merge_chain

text = """

## 📄 Project Documentation: AI Skill Chatbot for Freelancers

### 1. Introduction

Freelancing has become one of the fastest-growing work models in the global economy. According to recent industry reports, the global gig economy was valued at approximately **$674 billion in 2026** and is projected to reach **$2.5 trillion by 2035**, growing at a compound annual growth rate (CAGR) of **15.79%**. India alone has emerged as a major hub, with its gig workforce reaching **12 million in FY 2025** — a **55% increase in just four years** — and projected to grow to **23.5 million by 2029–30**.

Despite this growth, freelancers face significant challenges. Studies show that **52% of freelancers consider unstable project pipelines a major risk**, and **49% reported a worse pipeline compared to the previous year**. At the same time, **74% of freelancers now prioritize AI and automation skills**, reflecting a clear shift toward integrating artificial intelligence into freelance workflows.

This project — the **AI Skill Chatbot** — is designed to address this gap. It acts as a personal learning assistant for freelancers, generating structured study notes and practice quizzes on any given topic using multiple Large Language Models (LLMs) working in parallel.

### 2. Problem Statement

Freelancers often need to quickly learn new skills to stay competitive. However, existing learning platforms are:
- Too slow (long video courses)
- Too generic (not tailored to specific client needs)
- Too expensive (subscription-based)

There is a need for a lightweight, AI-powered tool that can instantly generate **concise notes** and **self-assessment quizzes** on any topic a freelancer wants to learn.

### 3. Proposed Solution

The AI Skill Chatbot uses **LangChain Expression Language (LCEL)** to orchestrate multiple LLMs in parallel. Given a topic, the system:
1. Generates **short notes** using one model (e.g., OpenRouter/GPT).
2. Generates a **quiz with questions and answers** using a second model (e.g., Hugging Face).
3. **Merges** both outputs into a single, unified study guide.

This parallel architecture reduces response time and improves output quality by leveraging the strengths of different models.

### 4. Technical Architecture

**Technologies Used:**
- **Python** — core programming language
- **LangChain** — for chaining and orchestrating LLM calls
- **OpenRouter API** — access to GPT, Gemini, and other models
- **Hugging Face Endpoint** — for open-source model inference
- **Dotenv** — for secure API key management

**Workflow:**
```
User Input (Topic)
        │
        ▼
┌───────────────────┐
│ RunnableParallel  │
├─────────┬─────────┤
│ Notes   │ Quiz    │
│ Chain   │ Chain   │
│ (Model1)│ (Model2)│
└────┬────┴────┬────┘
     │         │
     ▼         ▼
   Notes     Quiz
     │         │
     └────┬────┘
          ▼
    Merge Chain (Model2)
          │
          ▼
    Final Study Guide
```

### 5. Code Implementation

The core logic uses `RunnableParallel` to execute two chains simultaneously:

- **Chain 1** (`prompt_notes | model1 | parser`) → generates notes via OpenRouter.
- **Chain 2** (`prompt_quiz | model2 | parser`) → generates quiz via Hugging Face.
- **Merge Chain** (`prompt_merge | model2 | parser`) → combines both into one output.

This design is efficient, modular, and easy to extend with additional models or tasks (e.g., flashcards, summaries).

### 6. Freelancing Use Case

For a freelancer, this chatbot acts as a **just-in-time learning companion**:
- A web developer who gets a React project can instantly generate React notes + a quiz to test themselves.
- A data analyst preparing for a client interview can generate SQL practice questions.
- A designer learning Figma can get a quick refresher with self-assessment.

Because the tool is AI-driven, it scales across **any domain** without needing pre-built content.

### 7. Future Scope

- Add **voice output** for hands-free learning.
- Integrate **progress tracking** to monitor skill growth.
- Add **RAG (Retrieval-Augmented Generation)** to pull from trusted documentation.
- Deploy as a **mobile app** for on-the-go freelancers.
- Add **multi-language support** for global freelancers.

### 8. Conclusion

The AI Skill Chatbot demonstrates how modern LLM orchestration can solve a real-world problem for the growing freelance community. By combining factual market insights with a practical, parallel-chain AI architecture, this project offers both **technical value** and **real-world impact**.


"""


res = chain.invoke({'text': text})
print(res)

chain.get_graph().print_ascii()






