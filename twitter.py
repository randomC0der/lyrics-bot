import os
import sys
import logging
import tweepy

from datetime import date

#setup logging
logpath = "logs"
if not os.path.exists(logpath):
    os.mkdir(logpath)
logging.basicConfig(filename=os.path.join(logpath, str(date.today()) + '.log'), level=logging.INFO)
logging.info("Program started.")

try:
    auth = tweepy.OAuthHandler(os.environ["TwitterConsumerKey"], os.environ["TwitterConsumerSecret"])
    auth.set_access_token(os.environ["TwitterAccessToken"], os.environ["TwitterAccessSecret"])

except KeyError as missing_key:
    logging.error(f"Environment variable is missing: {missing_key}. Exiting program.")
    sys.exit(1)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    logging.info("Authentication OK")

    api.update_status("Hello, World!")

except tweepy.TweepError as twitter_error:
    error_json = twitter_error.response.text
    logging.error(f"Error {error_json.code}: {error_json.message}. Exiting program.")
    sys.exit(1)

except Exception as ex:
    logging.error(f"An unknown exception occurred: {ex}. Exiting program.")
    sys.exit(1)
