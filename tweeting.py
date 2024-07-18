import twint
import os
def get_tweets():
    
   # c.Format="tweet id:str({id}) | Username:{username}"
    c.Limit=5
    ##    c.Format="username"
##    c.Output="user"
    c.Output="tweets.txt"
    twint.run.Search(c)
    
def read_id():
    f=open("tweets.txt",'r',encoding="utf-8")
    f2=open("id.txt",'w')
    
    for line in f:
        for i in line:
            if(i==' '):
                break
            else:
                f2.write(i)
        f2.write("\n")
    f2.close()
    f.close()


def read_user():
    f=open("tweets.txt",'r',encoding="utf-8")
    f2=open("usernames.txt",'w')
    
    for line in f:
        for i in line:
            if(i=='>'):
                break
            else:
                f2.write(i)
        f2.write("\n")
    f2.close()
    f.close()


def get_user():
    f=open("usernames.txt",'r',encoding="utf-8")
    f1=open("getusers.txt",'w')
    for line in f:
        k=0
        for i in line:
            
            if(k==1):
                f1.write(i)
            if(i=='<'):
                k=1

    f1.close()
    f.close()


def find_followers():
    f1=open("getusers.txt",'r')
    f2=open("followers1.txt",'w')
    f1=list(f1)
    for item in f1:
        it=item.replace("\n",'')
        
        c=twint.Config()
        
        c.Username=it
        c.Limit=5
        c.Store_object=True
        print("lol")
        twint.run.Followers(c)
        followers = twint.output.follow_object
        
    
    f2.write(str(followers))
    f2.close()
    f1.close()
    









    
get_tweets()
read_id()
read_user()
get_user()
find_followers()
