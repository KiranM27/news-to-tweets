import os
import json
import requests
from dotenv import load_dotenv
from modules.constants import X_ACCESS_TOKEN, X_REFRESH_TOKEN, X_OAUTH2_CLIENT_ID

load_dotenv()  # take environment variables from .env.

class PostXThread:

    def __init__(self):
        self.x_access_token = os.getenv(X_ACCESS_TOKEN)
        self.x_refresh_token = os.getenv(X_REFRESH_TOKEN)
        self.x_oauth2_client_id = os.getenv(X_OAUTH2_CLIENT_ID)

    def get_x_info(self):
        url = "https://api.twitter.com/2/users/me"
        headers = {
            "Authorization": f"Bearer {self.x_access_token}"
        }

        response = requests.get(url, headers=headers)
        print(response.json())
        return response.json()
    
    def refresh_x_token(self):
        url = "https://api.twitter.com/2/oauth2/token"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        data = {
            "refresh_token": self.x_refresh_token,
            "grant_type": "refresh_token",
            "client_id": self.x_oauth2_client_id
        }

        response = requests.post(url, headers=headers, data=data)
        response = response.json()
    
    def refresh_tokens_if_needed(self):
        x_info = self.get_x_info()
        status = x_info.get('status', 200)
        if status:
            return self.refresh_x_token()


    def create_post(self, message: str, reply_to: str = None):

        self.refresh_tokens_if_needed()

        url = "https://api.twitter.com/2/tweets"
        headers = {
            "Content-type": "application/json",
            "Authorization": f"Bearer {self.x_access_token}"
        }

        data = {
            "text": message
        }

        if reply_to:
            data["in_reply_to_tweet_id"] = reply_to

        response = requests.post(url, headers=headers, data=json.dumps(data))
        return response.json()
    
