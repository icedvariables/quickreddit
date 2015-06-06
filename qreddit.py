import optparse

def main():
    print parseArguments()

def parseArguments():
    parser = optparse.OptionParser()
    parser.add_option("-s", "--subreddit", help="Specify subreddit", dest="subreddit")
    parser.add_option("-t", "--title", help="Specify title", dest="title")

    return parser.parse_args()


if __name__=="__main__":main()
