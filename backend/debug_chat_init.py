import sys
import os

# Ensure backend directory is in path if running from root
current = os.getcwd()
if current not in sys.path:
    sys.path.append(current)

try:
    print("Attempting to import chat_service...")
    # Adjust import based on where we run it. 
    # If running from backend folder:
    if os.path.exists("chat_service.py"):
        import chat_service
    else:
        from backend import chat_service
        
    print("Chat service imported successfully! Chain created.")
except Exception as e:
    print(f"CRITICAL ERROR during import: {e}")
    import traceback
    traceback.print_exc()
