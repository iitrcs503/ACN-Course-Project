 # Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# We use the file saved from last step as example
tweets_filename = '2016-06-03.txt'
tweets_file = open(tweets_filename, "r")
i = 0
for line in tweets_file:
    print "\n"
    i = i+1
    print "line.................",i
    try:
        # Read in one line of the file, convert it into a json object 
        tweet = json.loads(line.strip())
        if 'text' in tweet: # only messages contains 'text' field is a tweet
            print tweet['id'], ": Tweet id" # This is the tweet's id
            print tweet['created_at'], ": Time" # when the tweet posted
            print tweet['text'], ": Tweet" # content of the tweet
            print tweet['screen_name'],": Screen Name"
            print tweet['location'], " : location"         
            print tweet['user']['id'], ": UserId" # id of the user who posted the tweet
            print tweet['user']['name'], ": UserName" # name of the user, e.g. "Wei Xu"
            #print tweet['user']['screen_name'], ": accountName" # name of the user account, e.g. "cocoweixu"

            hashtags = []
            for hashtag in tweet['entities']['hashtags']:
            	hashtags.append(hashtag['text'])
            print hashtags, ": hashTag" 
 

    except:
        # read in a line is not in JSON format (sometimes error occured)
        continue
  
