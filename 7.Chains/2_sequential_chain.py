from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGroq(model='qwen/qwen3-32b')

parser = StrOutputParser()

template1 = PromptTemplate(
    template='Generate detailed report on the {topic}',
    input_variables=['topic']
)

template2 = PromptTemplate(
    template='Generate 5 point summary on the {text}',
    input_variables=['text']
)

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({'topic':'Unemployement in India'})
print(result)

chain.get_graph().print_ascii()