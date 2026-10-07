import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("HF_TOKEN")

if token:
    print("✅ HF_TOKEN encontrado")
    print(f"Longitud del token: {len(token)} caracteres")
else:
    print("❌ HF_TOKEN no encontrado")