import sys
import tweepy

consumer_key="tauLkEXjWF0GRSGNCqNO57Ho9"
consumer_secret="l7N96yBYQIerILtAQ2M093gEC1trrukXUFVfpPZ8mf1IyNZCqL"
access_key="1127256786224812032-5winXn01kC9DBa9zx26KFMc8bvxaEV"
access_secret="beJ90VuxN3Hvk1TQvhSURIxtLyZ4Mrk8DtSx4JwFBXF7P"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)


class CustomStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        if 'pollution' in status.text.lower():
            status.text=status.text.encode('unicode-escape').decode('utf-8')
            print (status.text)

    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream

sapi = tweepy.streaming.Stream(auth, CustomStreamListener())
#sapi = tweepy.streaming.Stream(auth, CustomStreamListener())
u=sapi.filter(track=['pollution'],languages=["en"])

u=u.encode('unicode-escape').decode('utf-8')
print(u)
