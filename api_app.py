import streamlit as st
import requests

st.title("AI Assistant for Men's Clothing")

user_query = st.text_input("What product are you looking for today?", placeholder="Type here...")

if st.button("Ask"):
    if user_query:
        with st.spinner("Processing..."):
            try:
                response = requests.post(
                    "http://127.0.0.1:8000/ask",
                    json={"query": user_query}
                )
                if response.status_code == 200:
                    st.success(response.json()["answer"])
                else:
                    st.error("Error from API")
            except Exception as e:
                st.error(f"Connection error: {e}")
    else:
        st.warning("Please enter a question!")
