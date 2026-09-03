import os

from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv()

hf_token = os.getenv("HF_TOKEN")
if not hf_token:
    raise RuntimeError("HF_TOKEN is missing. Add it to the .env file before running the agent.")

_endpoint = HuggingFaceEndpoint(
    repo_id=os.getenv("HF_MODEL", "HuggingFaceH4/zephyr-7b-beta"),
    task="text-generation",
    max_new_tokens=int(os.getenv("HF_MAX_NEW_TOKENS", "1024")),
    temperature=float(os.getenv("HF_TEMPERATURE", "0.1")),
    huggingfacehub_api_token=hf_token,
)

chat_model = ChatHuggingFace(llm=_endpoint)
