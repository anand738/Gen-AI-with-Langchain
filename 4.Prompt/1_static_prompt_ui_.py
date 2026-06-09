from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
import streamlit as st

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash',temperature=1.5)

st.header('Research Tool')
user_input = st.text_input('Enter user input')

if st.button('Summarize'):
    result = model.invoke(user_input)
    st.write(result.content)