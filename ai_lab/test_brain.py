import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# 1. Load the secret key from .env
load_dotenv()

# 2. Setup the "Brain"
# We use the 70B model because it's smarter at logic/SQL
llm = ChatGroq(
    temperature=0, 
    model_name="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

# 3. Test it
print("🤖 Awakening the Brain...")
try:
    response = llm.invoke("Hello! Are you ready to help me build Infinite BZ?")
    print(f"✅ Success! The Brain replied:\n{response.content}")
except Exception as e:
    print(f"❌ Error: {e}")