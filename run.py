# Python packages
from datetime import datetime, timezone
import time
import collections

# Importing user defined packages

from app import config, retweet

# Retrieve api object
api_obj = config.api_connect()



while True:
   retweet.retweet_tweet(api_obj)