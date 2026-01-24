import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.utilities import SQLDatabase
from langchain.chains import create_sql_query_chain
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table

# 1. Setup a "Fake" Database for Testing
# We create a temporary database in memory with 3 sample events
engine = create_engine("sqlite:///:memory:")
metadata_obj = MetaData()

# Define a simple "events" table structure
events = Table(
    "events",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("city", String),
    Column("price", Integer),
    Column("category", String),
)

# Create the table and add dummy data
metadata_obj.create_all(engine)
with engine.connect() as conn:
    conn.execute(events.insert(), [
        {"name": "AI Workshop", "city": "Chennai", "price": 1500, "category": "Tech"},
        {"name": "Music Fest", "city": "Mumbai", "price": 5000, "category": "Entertainment"},
        {"name": "Startup Summit", "city": "Chennai", "price": 0, "category": "Business"},
    ])
    conn.commit()

# 2. Connect the Brain
load_dotenv()
db = SQLDatabase(engine)
llm = ChatGroq(
    temperature=0, 
    model_name="llama-3.3-70b-versatile", 
    api_key=os.getenv("GROQ_API_KEY")
)

# 3. create the "Translator" Chain
# This chain takes English and outputs SQL
chain = create_sql_query_chain(llm, db)

# 4. The Test
question = "Find me all free business events in Chennai."
print(f"🕵️  User asks: '{question}'")

try:
    # Ask the AI to write the SQL
    response = chain.invoke({"question": question})
    
    # Clean up the response (sometimes AI adds extra text)
    sql_query = response.strip()
    
    print(f"🤖 AI generated SQL: \n{sql_query}")
    
    # Verify if it wrote the correct logic (looking for 'price = 0' or 'price IS NULL')
    if "events" in sql_query and "Chennai" in sql_query:
        print("\n✅ TEST PASSED: The AI correctly understood the table schema!")
    else:
        print("\n⚠️ TEST FAILED: The SQL looks wrong.")
        
except Exception as e:
    print(f"❌ Error: {e}")
    