#Go through an entire directory of JSON files, then show the number of tweets per day in date order
#Builds on https://github.com/eolienne/BroadwayTweets/blob/master/counterjson.py --> https://gist.github.com/edsu/af9c9ccacc7187437b49

import os
import json
from collections import Counter
time_format = '%a %b %d %H:%M:%S %z %Y'

path = './'
listing = os.listdir(path)
listing.remove('archive.log')

for infile in listing:
    newpath = path + infile
    for row in open(newpath):
        tweet = json.loads(row)
        created = datetime.datetime.strptime(tweet['created_at'], time_format)
        yield created.date().isoformat()

counts = Counter(created_at())

#Present the key/value pairs in date order
[(key, counts[key]) for key in sorted(counts.key())]     
