"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
import math

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

def maxSpentTimeOnPhone(records):
    longestCalls = {}

    for rec in records:
        # calling telephone
        if rec[0] in longestCalls:
            longestCalls[rec[0]] += int(rec[3])
        else:
            longestCalls[rec[0]] = int(rec[3])
            
        # receiving call
        if rec[1] in longestCalls:
            longestCalls[rec[1]] += int(rec[3])
        else:
            longestCalls[rec[1]] = int(rec[3])

    val = list(longestCalls.values())
    keys = list(longestCalls.keys())

    return keys[val.index(max(val))], max(val)

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(maxSpentTimeOnPhone(calls)[0], maxSpentTimeOnPhone(calls)[1]))

