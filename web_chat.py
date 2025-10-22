import os
from dotenv import load_dotenv
from openai import AzureOpenAI
import streamlit as st

# Load environment variables
load_dotenv()

# Initialize Azure OpenAI client
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-05-01-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")

# Streamlit UI configuration
st.set_page_config(page_title="💼 NewVision AI Chat", page_icon="🤖", layout="centered")

# Header section
st.title("💬 NewVision AI Chat Assistant")
st.markdown("""
Welcome to the **NewVision AI Consulting** demo chat app — powered by **Azure OpenAI GPT-4o-mini**.  
Type a question below to chat with your intelligent assistant.
""")

# User input
prompt = st.text_input("Ask me anything about AI, Azure, or consulting:", "")

if st.button("Submit"):
    if prompt.strip() == "":
        st.warning("Please enter a prompt before submitting.")
    else:
        try:
            response = client.chat.completions.create(
                model=deployment,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=300
            )
            st.success(response.choices[0].message.content)
        except Exception as e:
            st.error(f"Error: {e}")
