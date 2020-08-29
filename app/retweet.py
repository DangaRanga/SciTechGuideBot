"""This module handles retweeting tweets"""
import tweepy
from time import sleep

def retweet_tweet(api):
    """Reteet tweets with guidelines for freshers every 20 seconds
    
    This pauses for 30 seconds before pulling any more data from 
    the twitter api to prevent spam

    Args:
        api: The tweepy api object

    Returns:
        None

    """
    # Initialize key variables
    query = '#FacultyOfGreatness AND #FreshersGuide20 OR #FreshersGuide2020 OR #freshersguide2020'
    me = api.me()
    no_tweets = 20
    cursor_obj = tweepy.Cursor(api.search, q=(query),lang='en').items(no_tweets)
    for tweet in cursor_obj:
        # Skip entries from current user
        if tweet.user.id == me.id:
            continue
        print('\nTweet by: @' + tweet.user.screen_name)
        # Try exccept block to catch retweeted tweets
        try:
            # Retweet tweet as its found
            tweet.retweet()
        except tweepy.TweepError as e:
            print(e.reason)
            sleep(10)
        except StopIteration:
            break
        else:
            print('Retweeted the tweet')
            sleep(20)
    sleep(30)