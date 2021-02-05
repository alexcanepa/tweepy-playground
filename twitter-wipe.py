import json, os, tweepy

# Load API keys from json file
keypath = os.path.abspath("api-store.json")
with open(keypath, "r") as jsonfile:
    api_data = json.load(jsonfile)

# Authenticate user session
auth = tweepy.OAuthHandler(api_data["consumer"]["key"], api_data["consumer"]["secret"])
auth.set_access_token(api_data["access"]["token"], api_data["access"]["secret"])
api = tweepy.API(auth, timeout=5) # impatient
print("User Authenticated...")

# Print my 20 most recent tweets
myacct = api.me()
for tweet in tweepy.Cursor(api.user_timeline, id=myacct.id).items(5):
    print(tweet.id_str, tweet.text)

# # Write a new tweet
# api.update_status('tweepy + oauth!')

# Show account information
print(
    "\nTwitter account @{} (display name `{}`) has tweeted {} times.".format(
        myacct.screen_name, myacct.name, myacct.statuses_count
    )
)
