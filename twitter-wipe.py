import json
import os
import tweepy

# Load API keys from json file
keypath = os.path.abspath("api-store.json")
with open(keypath, "r") as jsonfile:
    api_data = json.load(jsonfile)

# Authenticate user session
auth = tweepy.OAuthHandler(api_data["consumer"]["key"], api_data["consumer"]["secret"])
auth.set_access_token(api_data["access"]["token"], api_data["access"]["secret"])
api = tweepy.API(auth, timeout=5) # impatient
print("User @{} Authenticated...\n".format(api.me().screen_name))


def wipe_tweet_history():
    """
    Erases any and all tweets posted by the authenticated user.
    """
    # Show account information
    print(
        "Twitter account {} (display name `{}`) has tweeted {} times to a whopping {} followers".format(
            api.me().screen_name,
            api.me().name,
            api.me().statuses_count,
            api.me().followers_count,
        )
    )
    # Print 5 most recent tweets
    print("You are about to delete your tweet history, which begins with: \n")
    for tweet in tweepy.Cursor(api.user_timeline).items(5):
        print("Tweet ID {}: {}".format(tweet.id_str, tweet.text))
    confirmation = input("Type 'yes' to confirm: ")
    # Require user input to continue
    if "yes" in confirmation.lower():
        print("Purging your history...")
        for tweet in tweepy.Cursor(api.user_timeline).items():
            api.destroy_status(tweet.id_str)
            print(
                "deleted tweet {} posted on {}".format(tweet.id_str, tweet.created_at)
            )
    else:
        print("exiting...")


if __name__ == "__main__":
    wipe_tweet_history()
