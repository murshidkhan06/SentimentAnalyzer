import os
import openai
import streamlit as st

openai.api_key = os.getenv("OPENAI_API_KEY")
st.header("Sentiment Analyzer")
text = st.text_area("Copy and Paste any statement")
button = st.button("Analyze and generate Sentiment")


def generate_auto_reponse(text):
    prompt = f"Identify and return the sentiment either Positive , Negative or Neutral in given text. text : {text}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = [{"role":"system", "content":"You are helpful sentiment analyzer that returns concise sentiment"},
                    {"role":"user", "content":prompt}
        ],
        temperature=0.7
    )
    print(response)
    return response.choices[0]['message']['content']

if text and button:
  with st.spinner(".......Generating Sentiment........"):
    reply = generate_auto_reponse(text)
    st.write(reply)
