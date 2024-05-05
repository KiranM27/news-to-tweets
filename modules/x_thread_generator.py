import os
import ast
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts.chat import ( ChatPromptTemplate )
from modules.constants import OPEN_AI_API_KEY, OPEN_AI_MODEL_TEMPERATURE, OPEN_AI_MODEL, THREAD_GENERATOR_SYSTEM_PROMPT, THREAD_GENERATOR_HUMAN_PROMPT, X_USERNAME

load_dotenv()  # take environment variables from .env.

class XThreadGenerator:
    def __init__(self):
        open_ai_api_key = os.getenv(OPEN_AI_API_KEY)
        x_username = os.getenv(X_USERNAME)
        chat = ChatOpenAI(temperature=OPEN_AI_MODEL_TEMPERATURE, model_name=OPEN_AI_MODEL, openai_api_key=open_ai_api_key)

        system = THREAD_GENERATOR_SYSTEM_PROMPT.format(x_username=x_username)
        human = "{input}"
        prompt = ChatPromptTemplate.from_messages([("system", system), ("human", human)])

        self.chain = prompt | chat

    def generate(self, industry: str, news_items: str):
        print(f"[INFO] Generating thread for the {industry} industry")

        query = THREAD_GENERATOR_HUMAN_PROMPT.format(industry=industry, news_items=news_items)
        response = self.chain.invoke({"input": query})

        print(f"[INFO] Generated thread for the {industry} industry")
        content = response.content

        # content is in the form of a string
        # we need to convert it to a list
        return ast.literal_eval(content)