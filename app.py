from modules.news_retreival import NewsRetreival
from modules.x_thread_generator import XThreadGenerator
from modules.constants import CRYPTO_INDUSTRY
from modules.post_x_thread import PostXThread
import time

def runner():
    retreiver = NewsRetreival()
    news = retreiver.get_news(CRYPTO_INDUSTRY)
    
    thread_generator = XThreadGenerator()
    thread = thread_generator.generate(CRYPTO_INDUSTRY, news)

    for (index, tweet) in enumerate(thread):
        print(f"[INFO] Tweet {index + 1}:")
        print("Character count: ", len(tweet))
        print(tweet, "\n")\
        
    print("\n Would you like to post this thread? (y/n): ")
    choice = input()
    if choice.lower() != "y":
        print("[INFO] Thread not posted")
        return

    past_tweet_id = None
    
    for (index, tweet) in enumerate(thread):
        time.sleep(1)
        print("[INFO] Posting tweet no: ", index + 1)
        post_x_thread = PostXThread()
        response = post_x_thread.create_post(tweet, past_tweet_id)
        data = response.get("data")
        past_tweet_id = data.get("id")

    print("[INFO] Thread posted successfully")


if __name__ == "__main__":
    runner()