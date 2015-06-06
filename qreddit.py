import optparse

def main():
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
    parser.add_option("-b", "--body", help="Specify post body", dest="body")

    return parser.parse_args()

def performAction(action, options):
    if(action == "textpost"):
        doTextPost(options)

if __name__=="__main__":main()
