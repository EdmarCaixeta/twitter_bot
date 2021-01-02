import tweepy
from time import sleep

def authentication():
    consumer_key = ""
    consumer_secret = ""
    access_token = ""
    access_token_secret = ""

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return auth

def interact(keyword, number_of_tweets):
    for tweet in tweepy.Cursor(api.search, keyword).items(number_of_tweets):
        try:
            tweet.retweet()
            tweet.favorite()
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break

def follow_back(application):
    for follower in tweepy.Cursor(application.followers).items():
        try:
            follower.follow()
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break

if __name__ == "__main__":
    auth = authentication()
    api = tweepy.API(auth)
    number_of_tweets =
    search_list = []
    while(True):
        follow_back(api)
        for item in search_list:
            interact(item, number_of_tweets)
        print("pause")
        sleep(1700)
        
