# Importing python related packages

import os
import tweepy


def api_connect():
    """Connects to the twitter API

    Args:
        None

    Returns:
        api: A twitter API Object
    """
    # Retrieve environment variables
    
    CONSUMER_API_KEY = os.environ.get('CONSUMER_API_KEY') 
    CONSUMER_API_SECRET_KEY = os.environ.get('CONSUMER_API_SECRET_KEY')
    ACCESS_TOKEN= os.environ.get('ACCESS_TOKEN') 
    ACCESS_TOKEN_SECRET = os.environ.get('ACCESS_TOKEN_SECRET')
    
    # Authenticate to twitter
    auth = tweepy.OAuthHandler(CONSUMER_API_KEY, CONSUMER_API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    
    # Create API Object
    api = tweepy.API(auth, 
                    wait_on_rate_limit=True,
                    wait_on_rate_limit_notify=True)
    return api

api_connect()

