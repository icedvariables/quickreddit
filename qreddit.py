import optparse, os, sys, json
from reddit import Reddit


class QReddit:
    def __init__(self):
        self.r = Reddit()
        (self.options, args) = self.parseArguments()

        if(len(args) < 1):
            print "Please specify type of action (textpost, linkpost, viewsub, createuser)"
            return

        self.action = args[0]

        if(self.options.username and self.options.password):
            self.user = {"username":self.options.username, "password":self.options.password}
        else:
            try:
                self.user = self.getUser()
            except IOError:
                print "No user was specified through --user and --password but could not find 'user.json'. Please either use createuser or use --user and --password."
                sys.exit()

    def parseArguments(self):
        parser = optparse.OptionParser()
        parser.add_option("-s", "--subreddit", help="Specify subreddit", dest="subreddit")
        parser.add_option("-t", "--title", help="Specify title", dest="title")
        parser.add_option("-b", "--body", help="Specify post body (for text post)", dest="body")
        parser.add_option("-l", "--link", help="Specify post link (for link post)", dest="link")
        parser.add_option("-u", "--user", help="Specify username", dest="username")
        parser.add_option("-p", "--pass", help="Specify password", dest="password")
        parser.add_option("-L", "--limit", help="Limit results (for view)", type="int", dest="limit")

        return parser.parse_args()

    def performAction(self):
        if(self.action == "textpost"):
            self.r.doTextPost(self.options, self.user)
        if(self.action == "linkpost"):
            self.r.doLinkPost(self.options, self.user)
        if(self.action == "viewsub"):
            self.r.doViewsub(self.options)
        if(self.action == "createuser"):
            self.createUser(self.options.username, self.options.password)

    def getUser(self):
        try:
            with open("user.json") as f:
                user = json.load(f)
        except IOError:
            raise e

        return user

    def createUser(self, username, password):
        with open("user.json", "w") as f:
            json.dump({"username":username, "password":password}, f)

if __name__=="__main__":
    a = QReddit()
    a.performAction()
