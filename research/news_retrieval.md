# News Retrieval

There are two main options to retrieve news from the internet. They are 
- Custom scraper + Bright Data API
- Serper Google Search API
- Perplexiy AI's Pro Search


# Custom Scraper + Bright Data API

[Link to Bright Data](https://brightdata.com/)

In the interest of time, and just because I don't really want to work with either Selenium or Puppeteer for this project, I am going to steer away from building a web scraper from scratch. Additionally, the Bright Data API costs some money as well, so no real incentive to use Bright Data and build a web scraper from scratch.

# Serper Google Search API

[Link to Serper Google Search API](https://serper.dev/)

The Serper Google Search API is on a credits model, meaning that you only pay for the number of credits that you use. And they have a free trial that gives you free 2500 queries. The rest of the pricing plan can be found below:

<br/>

![serper_pricing](../images/serper_pricing.png)

<br/>

A sample of the Serper Google Search API can be found below. It is nice that they have a direct way to get the news from the internet, but the sample response looks like it just returns the url of the news articles / other links from the google search api. Thus, in order to get the content of the sites that the google search api returns, you would need to use a web scraper on top of the Serper Google Search API. Additionally, they also have a limit of 10 links per query, so you would need to make multiple queries to get all the news articles that you want. 

<br/>

![serper_sample_res](../images/serper_sample_res.png)

<br/>

One interesting thing is that they also have a [LangChain integration](https://python.langchain.com/docs/integrations/providers/google_serper) which is pretty cool. Will come back to this at a later time when I have a bit more time to play around with LangChain and all of its integrations. 


# Perplexity AI's Pro Search 

This is a pretty interesting 

