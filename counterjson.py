#For JSON files that contain the results of Twarc scrapes

from collections import Counter
import datetime
import json

#Replace 'foo.json' with the json file that you want to use

CREATED_AT_FMT='%a %b %d %H:%M:%S %z %Y'
document = 'data/tweets-0001.json'
aList = []

#Test to see what the 'created_at' timestamp will look like
for row in open(document):
    a = json.loads(row)
    print(a['created_at'])

#Function for removing the time information from the timestamp
def date_from_created(created):
    if not isinstance(created,datetime.datetime):
        created = datetime.datetime.strptime(created, CREATED_AT_FMT)
    return created.date().isoformat()

#This counts the things
date_count=Counter(
    date_from_created(row['created_at']) 
    for row in aList
)
print(aList)
