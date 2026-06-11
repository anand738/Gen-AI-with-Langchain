from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGroq(model='qwen/qwen3-32b')

parser = StrOutputParser()

template = PromptTemplate(
    template='Generate 5 intresting fact about {topic}',
    input_variables=['topic']
)

chain = template | model | parser

result = chain.invoke({'topic':'cricekt'})
print(result)

chain.get_graph().print_ascii()