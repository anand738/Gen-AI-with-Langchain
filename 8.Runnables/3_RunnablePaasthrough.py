from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough
from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')
parser = StrOutputParser()
passthrough = RunnablePassthrough()

promp1 = PromptTemplate(
    template='generate a 1 tweet about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a 1 LinkedIn post on {topic}',
    input_variables=['topic']
)

joke_gen_chain = RunnableSequence(promp1,model,parser)



parallel_chain = RunnableParallel({
    'Joke': RunnablePassthrough(),
    'Explanation': RunnableSequence(prompt2, model,parser) 
})

final_chain = RunnableSequence(joke_gen_chain,parallel_chain)

print(final_chain.invoke({'topic':'Cricket'}))

