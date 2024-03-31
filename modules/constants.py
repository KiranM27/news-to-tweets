PERPLEXITY_API_KEY = 'PERPLEXITY_API_KEY' # the key used to access the perplexity api key in the .env file 
OPEN_AI_API_KEY = 'OPEN_AI_API_KEY' # the key used to access the openai api key in the .env file

# this has access to the internet but its not the most powerful model out there
PERPLEXITY_ONLINE_MODEL = 'sonar-medium-online'

# prompts 
# does not really give an entire paragraph, but might as well put it in the prompt 
PERPLEXITY_ONLINE_MODEL_SYSTEM_PROMPT = 'You are a helpful assitant whose job is to prvide the latest news from various industries. Give me atleast one paragraph about each of the latest news items.'
PERPLEXITY_ONLINE_MODEL_HUMAN_PROMPT = "What are some of the biggest news from the {industry} industry over the last few days?"

# temperatures 
PERPLEXITY_ONLINE_MODEL_TEMPERATURE = 0
OPEN_AI_MODEL_TEMPERATURE = 0.5

# industry names
CRYPTO_INDUSTRY = 'crypto and blockchain'
AI_INDUSTRY = 'artificial intelligence (ai)'