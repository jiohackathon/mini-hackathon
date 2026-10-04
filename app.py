import streamlit as st
from hello import say_hello
from ai import get_ai_response
from database import save_data, get_data

st.title("My Awesome Hackathon App 🚀")
name = st.text_input("What is your name?")

if st.button("Say Hello"):
    message = say_hello(name)
    st.success(message)

if st.button("Say Goodbye"):
    st.success("Goodbye! See you at the hackathon! 👋")

question = st.text_input("Ask a question")

if st.button("Ask AI"):
    answer = get_ai_response(question)
    st.write(answer)
if st.button("Save Question"):
    answer = get_ai_response(question)
    result = save_data(name, question, answer)
    st.success(result)

st.subheader("Saved Questions")
st.dataframe(get_data())