import tweepy
import csv
import pandas as pd
####input your credentials here
consumer_key = 'tauLkEXjWF0GRSGNCqNO57Ho9'
consumer_secret = 'l7N96yBYQIerILtAQ2M093gEC1trrukXUFVfpPZ8mf1IyNZCqL'
access_token = '1127256786224812032-5winXn01kC9DBa9zx26KFMc8bvxaEV '
access_token_secret = 'beJ90VuxN3Hvk1TQvhSURIxtLyZ4Mrk8DtSx4JwFBXF7P'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data
csvFile = open('ua.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#unitedAIRLINES",count=100,
                           lang="en",
                           since="2017-04-03").items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
