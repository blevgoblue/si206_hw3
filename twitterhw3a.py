# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.

import tweepy

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

# Send tweet here

