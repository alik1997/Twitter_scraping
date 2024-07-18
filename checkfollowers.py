import twint

def find_followers():
    c=twint.Config()
    c.Username="ATULMISHRA35"
    c.User_full=True
    twint.run.Followers(c)

find_followers()
