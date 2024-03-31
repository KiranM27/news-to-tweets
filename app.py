from modules.news_retreival import NewsRetreival
from modules.constants import CRYPTO_INDUSTRY

def runner():
    retreiver = NewsRetreival()
    news = retreiver.get_news(CRYPTO_INDUSTRY)
    print("The news is ", news)

if __name__ == "__main__":
    runner()