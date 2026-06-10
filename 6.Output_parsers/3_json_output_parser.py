from dotenv import load_dotenv
# Define the model
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

parser = JsonOutputParser()

template = PromptTemplate(
    template="""Answer the following query. {format_instructions}
                Query: Give me 5 facts about {topic}
                Return ONLY JSON.""",
    input_variables=["topic"],
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    }
)

chain = template | model | parser

result = chain.invoke({'topic':'black hole'})

print(result)