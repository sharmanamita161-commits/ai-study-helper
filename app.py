import streamlit as st
from openai import OpenAI

st.title("📚 AI Study Helper")

subject = st.selectbox("Select Subject", ["Maths", "Science", "English"])

question = st.text_input("Enter your question")

if st.button("Generate Answer"):
    if question:
        client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": f"You are a helpful {subject} teacher."},
                {"role": "user", "content": question}
            ]
        )

        st.write(f"Answer for {subject}:")
        st.write(response.choices[0].message.content)
