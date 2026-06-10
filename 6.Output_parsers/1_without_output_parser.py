from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

import os

os.environ['HF_HOME'] = r'D:\Anand Gupta\Data Science Final\GENAICX\huggingface_chache'

llm= HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task='text-generation'
)

model = ChatHuggingFace(llm=llm)


template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

template2 = PromptTemplate(
    template='Write a 5 line summary on following text. /n {text}',
    input_variables=['text']
)

prompt1 = template1.invoke({'topic':'black hole'})
result = model.invoke(prompt1)
print(result.content)
prompt2 = template2.invoke({'text':result.content})
result1 = model.invoke(prompt2)

print(result1.content)