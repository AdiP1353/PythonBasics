fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    line = line.rstrip()
    line = line.split()
    if len(line) < 3 or line[0] != "From":
        continue
    print(line[1])
    count += 1

print(f"There were {count} lines in the file with From as the first word")