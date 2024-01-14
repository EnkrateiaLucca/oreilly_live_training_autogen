# filename: get_tweets.py

import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("yourkey", "yourkey")
auth.set_access_token("yourkey", "yourkey")

# Create API object
api = tweepy.API(auth)

# Get the latest tweets from Andrej Karpathy
tweets = api.user_timeline(screen_name="karpathy", count=200, tweet_mode="extended")

for tweet in tweets:
    print(tweet.full_text)