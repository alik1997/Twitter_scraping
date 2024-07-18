import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentmod as s

#consumer key, consumer secret, access token, access secret.
ckey= "iFO16dJ2pwetYUraTWrJjldgP"
csecret="D44hTdDmi1trs7KhCqQRIBEFRonxn6cFCuuJFJtqlkjaEj8cEe"
atoken="1127256786224812032-yD8oEhksiEdAzEo5USt2IFe8YJnBKf"
asecret="JhjrdShozAEQGoySMSZk84VAYxdIoTVWbJjMDcm7HipUz"

class listener(StreamListener):
    
    def on_data(self, data):
        all_data = json.loads(data)
        tweet = all_data["text"]       
        sentiment_value, confidence = s.sentiment(tweet)
        tweet.encode('utf-8', 'ignore')
        if "RT" in tweet:
            pass
        else:
            tweets=open("tweets.txt","a",encoding="utf-8")
            tweets.write(tweet)
            tweets.write('\n')
            tweets.write(str(sentiment_value))
            tweets.write('\n')
            tweets.write(str(confidence))
            tweets.write('\n\n\n')
            tweets.close()
            print(tweet, sentiment_value, confidence)
            if confidence*100 >= 60:
                output = open("twitter-out.txt","a")
                output.write(sentiment_value)
                output.write('\n')
                output.close()
                return True


    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=['New Delhi air pollution'],languages=['en'])
