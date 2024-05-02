import os
from dotenv import load_dotenv
from langchain_community.chat_models import ChatPerplexity
from langchain_core.prompts import ChatPromptTemplate
from modules.constants import PERPLEXITY_API_KEY, PERPLEXITY_ONLINE_MODEL , NEWS_RETREIVAL_SYSTEM_PROMPT, NEWS_RETREIVAL_HUMAN_PROMPT, PERPLEXITY_ONLINE_MODEL_TEMPERATURE

load_dotenv()  # take environment variables from .env.

class NewsRetreival:
    def __init__(self):
        pplx_api_key = os.getenv(PERPLEXITY_API_KEY)
        chat = ChatPerplexity(temperature=PERPLEXITY_ONLINE_MODEL_TEMPERATURE, pplx_api_key=pplx_api_key, model=PERPLEXITY_ONLINE_MODEL)

        system = NEWS_RETREIVAL_SYSTEM_PROMPT
        human = "{input}"
        prompt = ChatPromptTemplate.from_messages([("system", system), ("human", human)])

        self.chain = prompt | chat

    def get_news(self, industry: str):
        print(f"[INFO] Retrieving news for the {industry} industry")
        query = NEWS_RETREIVAL_HUMAN_PROMPT.format(industry=industry)
        response = self.chain.invoke({"input": query})
        print(f"[INFO] Retrieved news for the {industry} industry")
        return response.content