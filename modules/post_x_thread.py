import os
import json
import requests
from dotenv import load_dotenv
from modules.constants import X_ACCESS_TOKEN, X_REFRESH_TOKEN, X_OAUTH2_CLIENT_ID, X_TOKENS_FILE
from modules.persist_dict_data import PersistDictData

load_dotenv()  # take environment variables from .env.

class PostXThread:

    def __init__(self):
        persist_dict_data = PersistDictData()
        data = persist_dict_data.load(X_TOKENS_FILE)

        self.x_access_token = data.get(X_ACCESS_TOKEN, None)
        self.x_refresh_token = data.get(X_REFRESH_TOKEN, None)
        self.x_oauth2_client_id = os.getenv(X_OAUTH2_CLIENT_ID)

        if not self.x_access_token or not self.x_refresh_token:
            raise Exception("X tokens not found")
        
    def get_x_info(self):
        url = "https://api.twitter.com/2/users/me"
        headers = {
            "Authorization": f"Bearer {self.x_access_token}"
        }

        response = requests.get(url, headers=headers)
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

        access_token = response.get("access_token")
        refresh_token = response.get("refresh_token")

        persist_dict_data = PersistDictData()
        persist_dict_data.save_key_value(X_TOKENS_FILE, X_ACCESS_TOKEN, access_token)
        persist_dict_data.save_key_value(X_TOKENS_FILE, X_REFRESH_TOKEN, refresh_token)
        
        self.x_access_token = access_token
        self.x_refresh_token = refresh_token
    
    def refresh_tokens_if_needed(self):
        x_info = self.get_x_info()
        status = x_info.get('status', 200)
        if status == 401:
            return self.refresh_x_token()


    def create_post(self, message: str, reply_to: str = None):

        self.refresh_tokens_if_needed()

        url = "https://api.twitter.com/2/tweets"
        headers = {
            "Content-type": "application/json",
            "Authorization": f"Bearer {self.x_access_token}"
        }

        data = {}
            
        if reply_to:
            data['reply'] = {}
            data['reply']["in_reply_to_tweet_id"] = reply_to

        data["text"] = message

        response = requests.post(url, headers=headers, data=json.dumps(data))
        return response.json()
    
