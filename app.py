import streamlit as st

st.title("📚 AI Study Helper")

subject = st.selectbox("Select Subject", ["Maths", "Science", "History"])
question = st.text_input("Enter your question")

if st.button("Generate Answer"):
    if question:
        st.write(f"Answer for {subject}:")
        st.write(f"This is a simple explanation for: {question}")
    else:
        st.warning("Please enter a question.")
