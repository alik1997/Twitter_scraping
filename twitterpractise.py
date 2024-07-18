from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import tweepy
import networkx as nx
import twint

consumer_key = "r1QkJMxNMjV4AbNfT3WMmiSPF"
consumer_secret = "vfIw2dh1AvODGDR0w7xsmvGfNBK3exerNt9r7CzBw21v4y4Tit"
access_key = "1127256786224812032-oiVmYytG6bGMMeH7upVKPUy472yINK"
access_secret = "k0167pGiHnARUJcIpvz8KgmOhRcKonZ1cJ2P4ibCxoQhV"
arrid=[]
arrfriendcount=[]
arrfollowercount=[]

G=nx.Graph()
class Listener(StreamListener):
    def on_data(self,data):
        user1=''
        dict1=json.loads(data)
        #global arrid,arrfriendcount,arrfollowercount,G
        #for i in range(10):
        #v=data.split(",").split(":")
        
        for k in dict1:
                if(k=='user'):
                    
                    for x in dict1[k]:
                        if(x=='screen_name'):
                            user1="sureshg64244904"
                            
                    c=twint.Config()
                    c.Username=user1
                    c.User_full=True
##                    print(type(c))
####                            #arrid+=[dict1[k][x]]
####                    #c=tweepy.Cursor(api.followers_ids,id=user1)
####                    #for page in c.pages():
####                        #page=tuple(page)
####                        #G.add_edge(user1,page)
                    twint.run.Followers(c)
##        #print(G.edges.data)
            
                    
##           
##        for j in dict1:
##                if(j=='followers_count'):
##                    print("lol")
##                    arrfollowercount+=[dict1[j]]
##                    
##        for i in dict1:
##                if(i=='friends_count'):
##                    arrfriendcount+=[dict1[i]]
                    
            
         # print(arrid)

        #print(data,end='\n\n\n')

    def on_error(self,status):
        print(status,end="\n")

if __name__=="__main__":

    listener=Listener()
    auth=OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_key,access_secret)
    api=tweepy.API(auth)
    stream=Stream(auth,listener)
    stream.filter(track=['ipl2019'])
