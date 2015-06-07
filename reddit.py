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

    def doViewsub(self, options):
        if not(options.limit):
            options.limit = 5

        sub = self.r.get_subreddit(options.subreddit)
        posts = sub.get_hot(limit=options.limit)

        for post in posts:
            name = str(post)
            if(len(name) >= 60): # use 79 instead of 80 because they're may be a trailing newline
                name = name[:57] + "..."
            else:
                name += " " * (60 - len(name)) # pad with spaces
            print name, ":", self.getPostId(post.short_link)

    def getPostId(self, url):
        return url.split("/")[-1]

    def getPostLink(self, postid):
        return "http://redd.it/"+postid
