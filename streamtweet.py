import datetime
# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = '1940115654-LtstQFsHMqkTrkm9felCY9m1CwyfMi9HEYD61Ko'
ACCESS_SECRET = 'XMIh5y8RCvdLjQJY7by6leaPe4z7GYCddVZEhKPmNKsWj'
CONSUMER_KEY = '5Lj6RY6thN2glQKZBM9qFSQ0U'
CONSUMER_SECRET = 'dz0VzRIVXFd2NiIECDO3XMGhukpgvGtQ3DanigNEw5mzfN10La'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter Streaming API
twitter_stream = TwitterStream(auth=oauth)

# Get a sample of the public data following through Twitter
iterator = twitter_stream.statuses.sample()

now = datetime.datetime.now()
today =  str(now).split(None, 1)[0]
fo = open(today+'.txt', 'a')

tweet_count = 1000
for tweet in iterator:
    tweet_count -= 1
    # Twitter Python Tool wraps the data returned by Twitter 
    # as a TwitterDictResponse object.
    # We convert it back to the JSON format to print/score
    fo.write(json.dumps(tweet)+ "\n")  
    
    # The command below will do pretty printing for JSON data, try it out
    # print json.dumps(tweet, indent=4)
       
    if tweet_count <= 0:
        break 


#fo.write("this is current date" + "\n")
