def remove_items(test_list, item):
 
    # remove the item for all its occurrences
    c = test_list.count(item)
    for i in range(c):
        test_list.remove(item)
 
    return test_list

def frequency_calculator(filein: str, fileout: str):
    fhand = open(filein,"r").read()

    wordl = fhand.split(" ")
    wordl.sort()

    print("Word list sorted")

    frequency_output = open(fileout,'a')


    frequency_list = []

    i = 0
    for thing in wordl:
        count = wordl.count(thing)
        frequency_list.append(f"{thing}: {count}\n")
        remove_items(wordl, thing)
        print(f"Iteration {i}")
        i += 1

    print("Frequency List Created")

    for thing in frequency_list:
        frequency_output.write(thing)

    print("Frequency List written")






