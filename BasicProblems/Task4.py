"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv, re

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.

One of the possible way of doing this is to first create a set: one for all call receivers, one for all text senders and one for all text receivers. 
Then you can simply run a for loop to check for each caller's 
presence in all of these sets and if it doesn't exist in any of them, then it becomes a telemarketer.
"""



def findTelemarketers(calls, texts):
  telemarketers = set()
  receivedCalls = set(receiveCall[1] for receiveCall in calls)
  sendTexts = set(sendText[0] for sendText in texts)
  receivedText = set(receivedText[1] for receivedText in texts)

  for caller in calls:
    if caller[0] not in receivedCalls and caller[0] not in sendTexts \
      and caller[0] not in receivedText:
      telemarketers.add(caller[0])
  return list(telemarketers)

print("These numbers could be telemarketers:")
for teleMarketers in sorted(findTelemarketers(calls, texts)):
   print(teleMarketers)
