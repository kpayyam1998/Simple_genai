import os
from dotenv import load_dotenv
import streamlit as st

from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain
import warnings
warnings.filterwarnings("ignore")
load_dotenv()

key=os.getenv("OPENAI_API_KEY")
llm=OpenAI(openai_api_key=key)
st.title("Simple Bot which gives the product company names")
p_name=st.text_input("Enter product name")
if p_name:
    prompt=PromptTemplate.from_template("Give me 5 unique company name which makes products {product_name}?")

    llmchain=LLMChain(llm=llm,prompt=prompt)


    st.write(llmchain.run(p_name))





