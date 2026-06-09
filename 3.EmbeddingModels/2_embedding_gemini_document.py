from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
)

documents = [
    "Delhi is capital of India",
    "Lucknow is capital of uttar pradesh",
    "London is capital of UK"
]

result = embeddings.embed_documents(documents)

print(len(result))
print(str(result))