# the bearer tokem that can be obtained from the twitter dev dashboard 
# cannot be used to post tweets.
# instead we need to get the acccess token by connecting via Oauth 2.0
import os
import urllib
import requests
from dotenv import load_dotenv
from modules.constants import X_OAUTH2_CLIENT_ID, X_REDIRECT_URL, X_TOKENS_FILE, X_ACCESS_TOKEN, X_REFRESH_TOKEN
from modules.persist_dict_data import PersistDictData

load_dotenv()  # take environment variables from .env.

class GetXTokens:

    def __init__(self):
        self.x_oauth2_client_id = os.getenv(X_OAUTH2_CLIENT_ID)

    def construct_auth_url_for_x(self):

        base_url = "https://twitter.com/i/oauth2/authorize"
        params = {
            "response_type": "code",
            "client_id": self.x_oauth2_client_id,
            "redirect_uri": X_REDIRECT_URL,
            "scope": "tweet.read users.read follows.read offline.access tweet.write like.read like.write",
            "state": "state",
            "code_challenge": "challenge",
            "code_challenge_method": "plain"
        }

        url = base_url + "?" + urllib.parse.urlencode(params)
        return url
    
    def exchange_code_for_tokens(self, code: str):
        
        url = "https://api.twitter.com/2/oauth2/token"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        data = {
            "code": code,
            "grant_type": "authorization_code",
            "client_id": self.x_oauth2_client_id,
            "redirect_uri": X_REDIRECT_URL,
            "code_verifier": "challenge"
        }

        # the data should be url encoded
        response = requests.post(url, headers=headers, data=data)
        return response.json()
    
    def runner(self):
        auth_url = self.construct_auth_url_for_x()
        print(f"Auth URL: {auth_url}")
        code = input("Enter the code: ")
        tokens = self.exchange_code_for_tokens(code)
        access_token = tokens.get("access_token")
        refresh_token = tokens.get("refresh_token")

        # save the tokens
        persist_dict_data = PersistDictData()
        persist_dict_data.save_key_value(X_TOKENS_FILE, X_ACCESS_TOKEN, access_token)
        persist_dict_data.save_key_value(X_TOKENS_FILE, X_REFRESH_TOKEN, refresh_token)

        print("The tokens have been saved.")
