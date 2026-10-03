import streamlit as st
from hello import say_hello
from ai import get_ai_response
from database import save_data

st.title("My Awesome Hackathon App 🚀")
name = st.text_input("What is your name?")

if st.button("Say Hello"):
    message = say_hello(name)
    st.success(message)

question = st.text_input("Ask a question")

if st.button("Ask AI"):
    answer = get_ai_response(question)
    st.write(answer)
if st.button("Save Data"):
    result = save_data(name, question)
    st.write(result)