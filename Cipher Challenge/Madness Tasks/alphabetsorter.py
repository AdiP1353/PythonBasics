fhand = open("finalcorpus.txt","r").read()

wordl = fhand.split(" ")
wordl.sort()

print("Word list sorted")

wordl = list(dict.fromkeys(wordl))
print("Duplicates removed")

fhand2 = open("alphabetcorpus.txt","a")
i = 0
for thing in wordl:
    fhand3 = open("alphabetcorpus.txt","r").read()
    if thing not in fhand3:
        fhand2.write(thing + '\n')
        print("it" + str(i))
        i += 1
print("List written")