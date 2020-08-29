# Importing user defined packages

from app import config, retweet

# Retrieve api object
api_obj = config.api_connect()


if __name__=='__main__':
   while True:
      retweet.retweet_tweet(api_obj)