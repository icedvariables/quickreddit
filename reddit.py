import praw, time, sys

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
            if(len(name) >= 60):
                name = name[:57] + "..."
            else:
                name += " " * (60 - len(name)) # pad with spaces
            print name, ":", post.id

    def doViewpost(self, options):
        post = self.r.get_submission(submission_id=options.postid)

        try:
            print post.score, "::", post.title
        except UnicodeEncodeError: # Happens on post with weird unicode characters
            print str(post)
        sys.stdout.write(post.domain + "\t")
        sys.stdout.write(str(time.time() - post.created_utc) + " seconds ago\t/u/" + str(post.author) + "\t")
        if(post.over_18):
            print "NSFW"

        print "\n", post.selftext
        print "=" * 80

        for comment in post.comments:
            try:
                sys.stdout.write("-" * 80)
                print comment.score, "::", comment.body
                print time.time() - comment.created_utc, "seconds ago\t/u/" + str(comment.author)
            except AttributeError: # if comment is a MoreComments object and not an actual comment
                print "\n", str(comment)
