import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

class PostXThread:

    def __init__(self):
        self.x_access_token = os.getenv("X_ACCESS_TOKEN")

    def create_post(self, message: str):

        url = "https://api.twitter.com/2/tweets"
        headers = {
            "Content-type": "application/json",
            "Authorization": f"Bearer {self.x_access_token}"
        }

        data = {
            "text": message
        }

        response = requests.post(url, headers=headers, data=json.dumps(data))
        return response.json()
    
    