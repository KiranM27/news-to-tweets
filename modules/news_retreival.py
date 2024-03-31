from langchain_community.chat_models import ChatPerplexity
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from constants import PERPLEXITY_API_KEY, PERPLEXITY_ONLINE_MODEL  
import os

load_dotenv()  # take environment variables from .env.

PPLXApiKey = os.getenv(PERPLEXITY_API_KEY)
chat = ChatPerplexity(temperature=0, pplx_api_key=PPLXApiKey, model=PERPLEXITY_ONLINE_MODEL)

system = "You are a helpful assitant whose job is to prvide the latest news from various industries. Give me atleast one paragraph about each of the latest news items."
human = "{input}"
prompt = ChatPromptTemplate.from_messages([("system", system), ("human", human)])

chain = prompt | chat
response = chain.invoke({"input": "What are some of the biggest news from the crypto industry over the last few days?."})
print(response.content)



