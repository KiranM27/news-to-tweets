import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from constants import OPEN_AI_API_KEY, OPEN_AI_MODEL_TEMPERATURE

load_dotenv()  # take environment variables from .env.

class XThreadGenerator:
    def __init__(self):
        open_ai_api_key = os.getenv(OPEN_AI_API_KEY)
        chat = ChatOpenAI(temperature=OPEN_AI_MODEL_TEMPERATURE, openai_api_key=open_ai_api_key)

        system = "You are a helpful assistant that translates {input_language} to {output_language}."
        human = "{text}"
        system_prompt = SystemMessagePromptTemplate.from_template(system)
        human_prompt = HumanMessagePromptTemplate.from_template(human)
        prompt = ChatPromptTemplate.from_messages([system_prompt, human_prompt])

        self.chain = prompt | chat

    def generate(self, input_language: str, output_language: str, text: str):
        print(f"[INFO] Translating {input_language} to {output_language}")
        response = self.chain.invoke(
            {
                "input_language": input_language,
                "output_language": output_language,
                "text": text,
            }
        )
        print(f"[INFO] Translated {input_language} to {output_language}")
        return response.content

if __name__ == "__main__":
    generator = XThreadGenerator()
    print(generator.generate("english", "spanish", "Hello, how are you?"))