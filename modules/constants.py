PERPLEXITY_API_KEY = 'PERPLEXITY_API_KEY' # the key used to access the perplexity api key in the .env file 
OPEN_AI_API_KEY = 'OPEN_AI_API_KEY' # the key used to access the openai api key in the .env file

# this has access to the internet but its not the most powerful model out there
PERPLEXITY_ONLINE_MODEL = 'sonar-medium-online' # models - https://docs.perplexity.ai/docs/model-cards
OPEN_AI_MODEL = 'gpt-3.5-turbo-0125' # models - https://platform.openai.com/docs/models/gpt-3-5-turbo

# prompts 
# does not really give an entire paragraph, but might as well put it in the prompt 
NEWS_RETREIVAL_SYSTEM_PROMPT = 'You are a helpful assitant whose job is to prvide the latest news from various industries. Give me atleast one paragraph about each of the latest news items.'
NEWS_RETREIVAL_HUMAN_PROMPT = "What are the 10 biggest news items from the {industry} industry over the last 2 days? Give me five sentences for each news item."

# keeping it to 240 so that there is some wiggle room
# also, am using twitter here instead of x since the model might not know what x is
THREAD_GENERATOR_SYSTEM_PROMPT = 'You are a copy writer for a twitter account that provides the latest news from various industries. Your role is to create create a twitter thread that summarizes the latest news. The first tweet should always be an overview of all the tweets and should contain hooks to draw the user in. The next few tweets should focus on one news item at a time. And Finally, the last tweet should be a call to action to like the tweet and follow the twitter account. Also, put in hashtags for each tweet and make sure that each tweet is less than 240 characters. Your output should strictly be in the form of a python list.'
THREAD_GENERATOR_HUMAN_PROMPT = "Here are some of the news items that I found for the {industry} industry. {news_items}. Feel free to drop ones that are not related to the industry or not very important."

# temperatures 
PERPLEXITY_ONLINE_MODEL_TEMPERATURE = 0
OPEN_AI_MODEL_TEMPERATURE = 0.5

# industry names
CRYPTO_INDUSTRY = 'crypto and blockchain'
AI_INDUSTRY = 'artificial intelligence (ai)'