import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts.chat import ( ChatPromptTemplate )
from constants import OPEN_AI_API_KEY, OPEN_AI_MODEL_TEMPERATURE, OPEN_AI_MODEL

load_dotenv()  # take environment variables from .env.

class XThreadGenerator:
    def __init__(self):
        open_ai_api_key = os.getenv(OPEN_AI_API_KEY)
        chat = ChatOpenAI(temperature=OPEN_AI_MODEL_TEMPERATURE, model_name=OPEN_AI_MODEL, openai_api_key=open_ai_api_key)

        system = "You are a helpful assistant that translates {input_language} to {output_language}."
        human = "{input}"
        prompt = ChatPromptTemplate.from_messages([("system", system), ("human", human)])

        self.chain = prompt | chat

    def generate(self, input_language: str, output_language: str, text: str):
        print(f"[INFO] Translating {input_language} to {output_language}")
        response = self.chain.invoke(
            {
                "input_language": input_language,
                "output_language": output_language,
                "input": text,
            }
        )
        print(f"[INFO] Translated {input_language} to {output_language}")
        return response.content

if __name__ == "__main__":
    generator = XThreadGenerator()
    print(generator.generate("english", "spanish", "Hello, how are you?"))