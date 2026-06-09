from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

llm = ChatGroq(model="qwen/qwen3-32b")

result = llm.invoke("Who is prime minister of india?")

print(result.content)
    