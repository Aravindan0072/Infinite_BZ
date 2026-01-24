import langchain
print(f"Langchain version: {langchain.__version__}")
print(f"Langchain path: {langchain.__path__}")
try:
    import langchain.chains
    print("langchain.chains imported successfully")
except ImportError as e:
    print(f"Error importing chains: {e}")

try:
    from langchain.chains import create_sql_query_chain
    print("create_sql_query_chain imported successfully")
except ImportError as e:
    print(f"Error importing create_sql_query_chain: {e}")
except Exception as e:
    print(f"Error: {e}")
