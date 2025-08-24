from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st

# Streamlit app title
st.title("Pirthika's Chat Bot")

# Input field
input_txt = st.text_input("Please enter your queries here...")

# Prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant. Your name is Pirthika's Assistant."),
    ("user", "User query: {query}")
])

# LLM using Ollama (make sure Ollama and the model are running locally)
llm = Ollama(model="llama2")

# Output parser
output_parser = StrOutputParser()

# Create chain
chain = prompt | llm | output_parser

# Run when user enters input
if input_txt:
    st.write(chain.invoke({"query": input_txt}))
