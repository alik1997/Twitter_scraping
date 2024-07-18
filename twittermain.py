from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

consumer_key = "tauLkEXjWF0GRSGNCqNO57Ho9"
consumer_secret = "l7N96yBYQIerILtAQ2M093gEC1trrukXUFVfpPZ8mf1IyNZCqL"
access_key = "1127256786224812032-5winXn01kC9DBa9zx26KFMc8bvxaEV"
access_secret = "beJ90VuxN3Hvk1TQvhSURIxtLyZ4Mrk8DtSx4JwFBXF7P"
arrid=[]
arrfriendcount=[]
arrfollowercount=[]


class Listener(StreamListener):
    def on_data(self,data):
        dict1=json.loads(data)
        global arrid,arrfriendcount,arrfollowercount
        #for i in range(10):
        
        for k in dict1:
                if(k=='id'):
                    arrid+=[dict1[k]]
                    
                
        for j in dict1:
                if(j=='followers_count'):
                    print("lol")
                    arrfollowercount+=[dict1[j]]
                    
        for i in dict1:
                if(i=='friends_count'):
                    arrfriendcount+=[dict1[i]]
                    
            
        print(arrid)
        print(arrfollowercount)
        print(arrfriendcount)
        #print(data,end='\n\n\n')
        return
        return True

    def on_error(self,status):
        print(status,end='\n\n\n')

if __name__=="__main__":

    listener=Listener()
    auth=OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_key,access_secret)

    stream=Stream(auth,listener)
    stream.filter(track=['pollution'])
