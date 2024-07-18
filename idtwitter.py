import twint

c = twint.Config()

c.Username = "twitter"
c.Store_csv = True
# CSV Fieldnames
c.Custom["tweet"] = ["id"]
# Name of the directory
c.Output = "twitter"

twint.run.Search(c)
