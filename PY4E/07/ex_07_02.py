
sum = 0.0
count = 0.0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        
        line = line[19 :]
        line = line.strip()
        line_float = float(line)
        
        sum += line_float
        count = count + 1
        
print(f"Average spam confidence: {sum/count}")