
import re

handle = open("text.txt")
sumlist = []
for line in handle:
    line = line.rstrip()
    numbers = (re.findall('[0-9]+' ,line))
    if len(numbers) <= 0:
         continue
    if len(numbers) > 0:
         for number in numbers:
              sumlist.append(float(number))
print(sum(sumlist))
 
          


        
