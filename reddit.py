import praw

class Reddit:
    def __init__(self, username, password, userAgent="QuickReddit: http://github.com/icedvariables/quickreddit /u/icedvariables"):
        self.r = praw.Reddit(user_agent=userAgent)
        self.r.login(username, password)

    def doTextPost(self, options):
        self.r.submit(options.subreddit, options.title, text=options.body)
