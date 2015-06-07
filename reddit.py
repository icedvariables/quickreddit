import praw

class Reddit:
    def __init__(self, userAgent="QuickReddit: http://github.com/icedvariables/quickreddit /u/icedvariables"):
        self.r = praw.Reddit(user_agent=userAgent)
        print "Created reddit object"

    def login(self, user, password):
        self.r.login(user, password)
        print "Logged in"

    def doTextPost(self, options, user):
        self.login(user["username"], user["password"])
        self.r.submit(options.subreddit, options.title, text=options.body)

    def doLinkPost(self, options, user):
        self.login(user["username"], user["password"])
        self.r.submit(options.subreddit, options.title, url=options.link)
