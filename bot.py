import tweepy

def authentication():
    consumer_key = "X"
    consumer_secret = "X"
    access_token = "X"
    access_token_secret = "X"

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

if __name__ == "__main__":
    auth = authentication()
    api = tweepy.API(auth)
    number_of_tweets = 5
    search_list = []
    for item in search_list:
        interact(item, number_of_tweets)
    