"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

def countNumbers(texts, calls):
    memory = set()
    
    for txt, call in zip(texts, calls):
        memory.add(txt[0])
        memory.add(txt[1])
        memory.add(call[0])
        memory.add(call[1])
    return memory
    
print("There are {} different telephone numbers in the records.".format(len(countNumbers(texts, calls))))
