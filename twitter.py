import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("todo", "todo")
auth.set_access_token("todo", "todo")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")
