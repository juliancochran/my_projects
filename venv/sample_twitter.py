import tweepy
from tweepy import OAuthHandler

consumer_key = 'RUw2gUROglc2tOzw6Zna4O15c'
consumer_secret = 'UuQfhCijIhMw2ndjcd5rGxEpbxKLL0BFYCvlU2alK2eXzWNhUl'
access_token = '304613716-PFXz6wYRkusCB7s32xaAJdBi6HlTcwya0LdgSOJo'
access_secret = 'P65ImDw67XYmogD1cfSKIxfSoXfTlaw1mxtnIEVSzT73x'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    print(status.text)