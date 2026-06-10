from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()

class Person(BaseModel):
    name: str = Field(description="Name of Person")
    age: int = Field(gt=18, description="Age of Person")
    city: str = Field(description="City of Person")

parser = PydanticOutputParser(pydantic_object=Person)

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

prompt = PromptTemplate(
    template="""
Generate details of a fictional Indian person.
{format_instructions}
""",
    input_variables=[],
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    }
)

chain = prompt | model | parser

result = chain.invoke({})

print(result)
print(result.model_dump())