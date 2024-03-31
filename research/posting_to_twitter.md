# Posting to Twitter

Twitter does not have a direct API to post threads on twitter. Thus, the way to go about posting threads to twitter, is to post the first tweet and then reply to that tweet with the second tweet in the thread and so on until the thread is complete. Make sure to the `reply` object in the api call, which is a json containing the information of the tweet that you are replying to. This should allow you to chain tweets together and create a thread.

- [Link to Twitter API Docs](https://developer.twitter.com/en/docs/twitter-api/tweets/manage-tweets/api-reference/post-tweets)
- [Link to X Developer Blog talking about the above](https://devcommunity.x.com/t/is-there-a-way-to-post-a-twitter-thread-in-api/174942)