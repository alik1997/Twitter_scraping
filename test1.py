from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import tweepy
import networkx as nx
import json
import twint

consumer_key = "r1QkJMxNMjV4AbNfT3WMmiSPF"
consumer_secret = "vfIw2dh1AvODGDR0w7xsmvGfNBK3exerNt9r7CzBw21v4y4Tit"
access_key = "1127256786224812032-oiVmYytG6bGMMeH7upVKPUy472yINK"
access_secret = "k0167pGiHnARUJcIpvz8KgmOhRcKonZ1cJ2P4ibCxoQhV"



class Listener(StreamListener):
    G=nx.Graph()
    def on_data(self,data): 
        #print(data)
        user=''
        data=json.loads(data)
        for k in data:
            if(k=='user'):
                #print(data[k])
                for x in data[k]:
                    if(x=='screen_name'):
                        user=data[k][x]
                c=twint.Config()
                c.Username=user
                c.User_full = True
##                c.Format = "Username: {username} | Bio: {bio} | Url: {url}"
                #c.Output = "users.txt"
                twint.run.Followers(c)
                
    def on_error(self,status):
        print(status,end='\n\n\n')

if __name__=="__main__":

    listener=Listener()
    auth=OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_key,access_secret)
    api=tweepy.API(auth)
    stream=Stream(auth,listener)
    stream.filter(track=['ipl2019'])
