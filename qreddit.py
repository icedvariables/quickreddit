import optparse, os, json
from reddit import Reddit


class QReddit:
    def __init__(self):
        self.r = Reddit()
        self.users = self.getUsers()
        (self.options, args) = self.parseArguments()

        if(len(args) < 1):
            print "Please specify type of action (textpost, linkpost)"
            return

        self.action = args[0]

    def parseArguments(self):
        parser = optparse.OptionParser()
        parser.add_option("-s", "--subreddit", help="Specify subreddit", dest="subreddit")
        parser.add_option("-t", "--title", help="Specify title", dest="title")
        parser.add_option("-b", "--body", help="Specify post body (for text post)", dest="body")
        parser.add_option("-l", "--link", help="Specify post link (for link post)", dest="link")

        return parser.parse_args()

    def performAction(self):
        if(self.action == "textpost"):
            self.r.doTextPost(self.options)
        if(self.action == "linkpost"):
            self.r.doLinkPost(self.options)

    def getUsers(self):
        files = self.getUserFiles()
        userData = []

        for filename in files:
            with open(filename) as f:
                try:
                    userData.append(json.load(f))
                except ValueError, e:
                    print "Invalid user file:", e
                    sys.exit()

        return userData

    def getUserFiles(self, directory="users"):
        userFiles = []

        for file in os.listdir(directory):
            if(file.split(".")[-1] == "user"):
                userFiles.append(os.path.join(directory, file))

        return userFiles

if __name__=="__main__":
    a = QReddit()
    a.performAction()
