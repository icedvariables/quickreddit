import optparse, os, json
from reddit import Reddit

r = Reddit()

def main():
    users = getUsers()
    print users
    (options, args) = parseArguments()

    if(len(args) < 1):
        print "Please specify type of action (textpost, linkpost)"
        return

    action = args[0]

    performAction(action, options)

def parseArguments():
    parser = optparse.OptionParser()
    parser.add_option("-s", "--subreddit", help="Specify subreddit", dest="subreddit")
    parser.add_option("-t", "--title", help="Specify title", dest="title")
    parser.add_option("-b", "--body", help="Specify post body (for text post)", dest="body")
    parser.add_option("-l", "--link", help="Specify post link (for link post)", dest="link")

    return parser.parse_args()

def performAction(action, options):
    if(action == "textpost"):
        r.doTextPost(options)
    if(action == "linkpost"):
        r.doLinkPost(options)

def getUsers():
    files = getUserFiles()
    userData = []

    for filename in files:
        with open(filename) as f:
            try:
                userData.append(json.load(f))
            except ValueError, e:
                print "Invalid user file:", e
                sys.exit()

    return userData

def getUserFiles(directory="users"):
    userFiles = []

    for file in os.listdir(directory):
        if(file.split(".")[-1] == "user"):
            userFiles.append(os.path.join(directory, file))

    return userFiles

if __name__=="__main__":main()
