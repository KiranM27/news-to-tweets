from modules.news_retreival import NewsRetreival
from modules.x_thread_generator import XThreadGenerator
from modules.constants import CRYPTO_INDUSTRY

def runner():
    retreiver = NewsRetreival()
    news = retreiver.get_news(CRYPTO_INDUSTRY)
    
    thread_generator = XThreadGenerator()
    thread = thread_generator.generate(CRYPTO_INDUSTRY, news)
    print(thread)

if __name__ == "__main__":
    runner()