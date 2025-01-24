from langchain_openai import ChatOpenAI
# this is required because we are using this chatmodel 
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")
#langsmith tracking
os.environ['LANGCHAIN_TRACING_V2'] ='true'
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')

# prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ('system','you are assistant.please response to the given queries'),
        ('users',"question:{question}")
    ]
)

##streamlit framework
st.title('Langchain demo with openai')
input_text = st.text_input("search topic that you want!!")

llm = ChatOpenAI(model='llama2')
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))