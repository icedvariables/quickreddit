import optparse

def main():
    print parseArguments()

def parseArguments():
    parser = optparse.OptionParser()
    parser.add_option("-s", "--subreddit", help="Specify subreddit", dest="subreddit")
    parser.add_option("-t", "--title", help="Specify title", dest="title")
    parser.add_option("-b", "--body", help="Specify post body", dest="body")

    return parser.parse_args()


if __name__=="__main__":main()
