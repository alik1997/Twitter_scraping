import tweepy 
  
# Fill the X's with the credentials obtained by  
# following the above mentioned procedure.

consumer_key = "eKloOsXfNKRPFRQP75HoypAe8" 
consumer_secret = "cftMlVM8VRJ5d9263fsLUD4omPDqFUUyv0nfohkTkYTmwfI2JC"
access_key = "1127256786224812032-h9H4eC9nNRrQzDgH8fiZE6ywjnvg2Y"
access_secret = "8hLrRijXMWTN9RTu8o3rLhlgmRk2RQgxViJcZgiykAYyi"



  
# Function to extract tweets 
def get_tweets(): 
          
         #Authorization to consumer key and consumer secret 
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
  
        # Access to user's access key and access secret 
        auth.set_access_token(access_key, access_secret) 
  
        # Calling api 
        api = tweepy.API(auth) 
        class MyStreamListener(tweepy.StreamListener):

            def on_status(self, status):
                status.text=status.text.encode('unicode-escape').decode('utf-8')
                print(status)

##            def on_error(self, status_code):
##                if status_code == 420:
##                    #returning False in on_data disconnects the stream
##                    return False

        myStreamListener = MyStreamListener()
        myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
        

        myStream.filter(track=['pollution'],languages=["en"])
        #print(u)
        #u=u.encode('unicode-escape').decode('utf-8')
        # myStream.filter(follow=["868039570331512833"])
        
        # 200 tweets to be extracted 
##        number_of_tweets=200
##        tweets = api.user_timeline(screen_name=username) 
##  
##        # Empty Array 
##        tmp=[]  
##  
##        # create array of tweet information: username,  
##        # tweet id, date/time, text 
##        tweets_for_csv = [tweet.text for tweet in tweets] # CSV file created  
##        for j in tweets_for_csv: 
##  
##            # Appending tweets to the empty array tmp 
##            tmp.append(j)  
##  
##        # Printing the tweets 
##        print(tmp) 
##  
  
# Driver code 
if __name__ == '__main__': 
  
    # Here goes the twitter handle for the user 
    # whose tweets are to be extracted. 
    get_tweets()  
