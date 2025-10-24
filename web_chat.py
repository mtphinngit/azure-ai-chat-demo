import os
from dotenv import load_dotenv
from openai import AzureOpenAI
import streamlit as st
from datetime import datetime   # ✅ Added import for current date/time

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
st.set_page_config(page_title="Azure AI Chat Demo", page_icon="🤖", layout="centered")
st.title("🧠 NewVision AI Chat Assistant")
st.markdown("""
Welcome to the **NewVision AI Consulting** demo chat app — powered by **Azure OpenAI GPT-4o-mini**.  
Type a question below to chat with your intelligent assistant.
""")

# User input
prompt = st.text_input("Ask me anything about AI, Azure, or consulting:")

if prompt:
    # ✅ Inject current date/time into system message
    current_date = datetime.now().strftime("%B %d, %Y")
    system_message = f"Today’s date is {current_date}. Always use this as the current date when answering."

    # Send messages to Azure OpenAI
    response = client.chat.completions.create(
        model=deployment,
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": prompt}
        ]
    )

    # Display response
    st.write("**Response:**")
    st.write(response.choices[0].message.content)
