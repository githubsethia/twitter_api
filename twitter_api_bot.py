#Documentation: http://docs.tweepy.org/en/latest/getting_started.html
#keys and token: https://developer.twitter.com/en/apps

import tweepy
import time

consumer_key = 'XXXXXXXXXXXXXXXXXXXXX'
consumer_secret = 'XXXXXXXXXXXXXX' 
access_token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
access_token_secret = 'XXXXXXXXXXXXXXXXXXXXXXX'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#reading public tweets on the homepage
# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

# user = api.me()
# print(user.name)
# print(user.screen_name)
# print(user.followers_count)
#print(dir(user))

#Bot - follow the follower

#Handling the rate limit using cursor

def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except StopIteration:
            return
        except tweepy.RateLimitError:
            time.sleep(1 * 60)

# print(type(tweepy.Cursor(api.followers).items()))
for follower in limit_handled(tweepy.Cursor(api.followers).items()):
    print(follower.name)
    follower.follow()

#search for contents related with particular keyword and like it
search_str = 'python'
num = 2

for tweet in limit_handled(tweepy.Cursor(api.search,search_str).items(num)):
    try:
        tweet.favorite()
        print('I liked that tweet')
    except tweepy.TweepError as err:
        print(err)


