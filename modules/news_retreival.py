from langchain_community.chat_models import ChatPerplexity
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.

perplexity_api_key = os.environ.get("PERPLEXITY_API_KEY");
print(perplexity_api_key)


