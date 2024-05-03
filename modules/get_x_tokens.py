# the bearer tokem that can be obtained from the twitter dev dashboard 
# cannot be used to post tweets.
# instead we need to get the acccess token by connecting via Oauth 2.0
import os
import urllib
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.


def construct_auth_url_for_x():

    x_oauth2_client_id = os.getenv('X_OAUTH2_CLIENT_ID')

    base_url = "https://twitter.com/i/oauth2/authorize"
    params = {
        "response_type": "code",
        "client_id": x_oauth2_client_id,
        "redirect_uri": "http://127.0.0.1",
        "scope": "tweet.read users.read follows.read offline.access",
        "state": "state",
        "code_challenge": "challenge",
        "code_challenge_method": "plain"
    }

    url = base_url + "?" + urllib.parse.urlencode(params)
    return url

print(construct_auth_url_for_x())