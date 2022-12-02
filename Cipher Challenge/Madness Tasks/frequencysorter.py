fhand = open("finalcorpus.txt","r").read()

wordl = fhand.split(" ")
wordl.sort()

frequency_output = open("frequency_output.txt",'a')
print("Word list sorted")
word_no_dupes = list(dict.fromkeys(wordl))
word_count = len(word_no_dupes)
print(f"{word_count} Unique words detected")
frequencies = []
for i, thing in enumerate(word_no_dupes):
    count = wordl.count(thing)
    #frequency_output.write(f"{thing}:{count},\n")
    frequencies.append(f"{thing}: {count},")
    print("In progress:" + str(i/word_count*100) + "%")

frequency_output.writelines(frequencies)
