
#The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.





shen = dict()
senders = []
maximum = -1


    
name = input("Enter file:")

if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

for line in handle:
    line = line.rstrip()
    if len(line) < 1 or line.startswith("From: ") == False:
        continue
    else:
        words = line.split()
        for word in words:
            if word != "From:":
                senders.extend(words)
            else:
                continue       
        for word in senders:
            if word == "From:":
                senders.remove("From:")
            else:
                shen[word] = shen.get(word, 0) + 1
print(shen) 

        
            

          