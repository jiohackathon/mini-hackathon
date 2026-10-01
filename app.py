import streamlit as st

st.title("My First Hackathon App")

if "click_count" not in st.session_state:
    st.session_state.click_count = 0

name = st.text_input("What's your name?")

if st.button("Say Hello"):
    st.session_state.click_count += 1
    st.write(f"Hello {name}! 🚀")

st.write(f"Say Hello clicked: {st.session_state.click_count} time(s)")
