from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import TextLoader
from dotenv import load_dotenv
load_dotenv()

model = ChatGroq(model="qwen/qwen3-32b")
parser = StrOutputParser()

prompt = PromptTemplate(
    template='Write a summary for the folloling poem in 5 lines - \n {poem}',
    input_variables=['poem']
)

loader = TextLoader(r'9.DocumentLoaders\cricket.txt',encoding='utf-8')

docs = loader.load()

print(type(docs))
print(len(docs))
# print(docs[0].page_content)


chain = prompt | model | parser

print(chain.invoke({'poem':docs[0].page_content}))