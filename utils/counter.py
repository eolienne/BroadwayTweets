#For JSON files that contain the results of Twarc scrapes. This file could be stored in your Twarc utils folder
#To execute: python3 utils/counter.py foo.json

from __future__ import print_function

from collections import Counter
import datetime
import json
import fileinput

#Replace 'foo.json' with the json file that you want to use

CREATED_AT_FMT='%a %b %d %H:%M:%S %z %Y'
aList = []

#Store these created_at elements as a list
for row in fileinput.input():
    a = json.loads(row)  
    aList.append(a['created_at'])

#Function for removing the time information from the timestamp
def date_from_created(created):
    if not isinstance(created,datetime.datetime):
        created = datetime.datetime.strptime(created, CREATED_AT_FMT)
    return created.date().isoformat()

#This counts the things
date_count=Counter(
    date_from_created(row) 
    for row in aList
)

print(date_count)
