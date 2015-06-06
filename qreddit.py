import optparse

def main():
    print parseArguments()

def parseArguments():
    parser = optparse.OptionParser()
    parser.add_option("-s", "--subreddit", help="Specify subreddit",
                      action="store", type="string", dest="subreddit")
    parser.add_option("-t", "--title", helpt="Specify title",
                      action="store", type="string", dest="title")

    return parser.parse_args()


if __name__=="__main__":main()
