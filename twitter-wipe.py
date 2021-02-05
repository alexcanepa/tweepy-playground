import json, os, tweepy

# Load API keys from json file
keypath = os.path.abspath("api-store.json")
with open(keypath, "r") as jsonfile:
    api_data = json.load(jsonfile)

# Authenticate user session
auth = tweepy.OAuthHandler(api_data["consumer"]["key"], api_data["consumer"]["secret"])
auth.set_access_token(api_data["access"]["token"], api_data["access"]["secret"])
api = tweepy.API(auth)

public_tweets = api.user_timeline(user_id=api_data["username"])
for tweet in public_tweets:
    print(tweet.text)
