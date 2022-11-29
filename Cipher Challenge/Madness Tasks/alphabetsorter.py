fhand = open("finalcorpus.txt","r").read()

wordl = fhand.split(" ")
wordl.sort()

wordl = list(dict.fromkeys(wordl))
print(wordl)

# fhand2 = open("alphabetcorpus.txt","a")

# for thing in wordl:
#     fhand3 = open("alphabetcorpus.txt","r").read()
#     if thing not in fhand3:
#         fhand2.write(thing + '\n')
    