from cgitb import text
import re

handle = open("text.txt")

for line in handle:
    line = line.rstrip()
    numbers = (re.findall('[0-9]+' ,line))
    print(numbers)
    if len(numbers) > 0:
         continue
    # else:
    #     banana.extend(numbers)
        
