from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

llm = ChatGroq(model="llama-3.3-70b-versatile")

result = llm.invoke("Who is prime minister of india?")

print(result.content)
    