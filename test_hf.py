import os

from dotenv import load_dotenv
from huggingface_hub import InferenceClient


load_dotenv()

token = os.getenv("HF_TOKEN")

if not token:
    raise RuntimeError("HF_TOKEN no encontrado")


client = InferenceClient(
    api_key=token,
    provider="auto",
)


response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {
            "role": "user",
            "content": "Hola. Preséntate brevemente en español.",
        }
    ],
)


print(response.choices[0].message.content)