# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.

import tweepy
from textblob import TextBlob

# From sample twittercode
# Unique code from Twitter
access_token = "505320830-d73fh2e8RTtabRloKUbAX9jPRjKEyNmuwJEzp5YV"
access_token_secret = "2nQgjPPdtZIUnQH6mJ6K2DjiIvJqF08wkv89oyavwtN0b"
consumer_key = "dZ2HIpAcyUmMdEPMjHzItYUKl"
consumer_secret = "btNxeBAw38HMQdotWVEyLvKkTgufMoS6hdeyO349jgotXLucFm"

# Boilerplate code here
# Create tweepy
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)

# Now we can Create Tweets, Delete Tweets, and Find Twitter Users

# Search for tweets
for tweet in api.search("michigan"):
    # Loop over all tweets in search results
    # Print tweet
    print(tweet.text, "\n\n")
