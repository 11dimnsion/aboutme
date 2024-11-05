# from langchain import LLMChain
# from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

# Define a prompt template
template = """
You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. 
If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise.
Question: {question} 
Context: {context} 
Answer:
"""

rag_prompt = PromptTemplate(
    input_variables=["context", "question"],
    template=template
)
