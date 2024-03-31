PERPLEXITY_API_KEY = 'PERPLEXITY_API_KEY' # the key used to access the perplexity api key in the .env file 

# this is the most powerful model available on the perplexity api
# thus, it is also the most expensive one. so double check if you want to use this model
PERPLEXITY_ONLINE_MODEL = 'pplx-70b-online'

# prompts 
# does not really give an entire paragraph, but might as well put it in the prompt 
PERPLEXITY_ONLINE_MODEL_SYSTEM_PROMPT = 'You are a helpful assitant whose job is to prvide the latest news from various industries. Give me atleast one paragraph about each of the latest news items.'
PERPLEXITY_ONLINE_MODEL_HUMAN_PROMPT = "What are some of the biggest news from the {industry} industry over the last few days?"

# industry names
CRYPTO_INDUSTRY = 'crypto and blockchain'
AI_INDUSTRY = 'artificial intelligence (ai)'