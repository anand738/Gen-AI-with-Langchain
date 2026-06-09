from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
llm = ChatGoogleGenerativeAI(model='gemini-2.5-flash',temperature=1.5)

result = llm.invoke("Write poem on cricekt in 5 lines")
print(result.content)