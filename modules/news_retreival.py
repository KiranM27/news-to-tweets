from langchain_community.chat_models import ChatPerplexity
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from modules.constants import PERPLEXITY_API_KEY, PERPLEXITY_ONLINE_MODEL , PERPLEXITY_ONLINE_MODEL_SYSTEM_PROMPT, PERPLEXITY_ONLINE_MODEL_HUMAN_PROMPT
import os

load_dotenv()  # take environment variables from .env.

class NewsRetreival:
    def __init__(self):
        pplx_api_key = os.getenv(PERPLEXITY_API_KEY)
        self.chat = ChatPerplexity(temperature=0, pplx_api_key=pplx_api_key, model=PERPLEXITY_ONLINE_MODEL)
        self.system = PERPLEXITY_ONLINE_MODEL_SYSTEM_PROMPT
        self.human = "{input}"
        self.prompt = ChatPromptTemplate.from_messages([("system", self.system), ("human", self.human)])
        self.chain = self.prompt | self.chat

    def get_news(self, industry: str):
        print(f"[INFO] Retrieving news for the {industry} industry")
        query = PERPLEXITY_ONLINE_MODEL_HUMAN_PROMPT.format(industry=industry)
        response = self.chain.invoke({"input": query})
        print(f"[INFO] Retrieved news for the {industry} industry")
        return response.content