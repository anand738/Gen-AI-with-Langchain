from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

hf_token = os.getenv("HUGGINGFACE_ACCESS_TOKEN")

if not hf_token:
    raise ValueError("HUGGINGFACE_ACCESS_TOKEN not found in .env file")

# Create Hugging Face endpoint
llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation",
    huggingfacehub_api_token=hf_token,
    max_new_tokens=256,
    temperature=0.7
)

chat_model = ChatHuggingFace(llm=llm)
response = chat_model.invoke("Who is Virat Kohli?")

print("\nResponse:\n")
print(response.content)