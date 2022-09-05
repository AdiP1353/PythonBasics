fname = input("Enter a file name: ")
try:
    fhandle = open(fname)
except:
    print(f"Cannot open file: FILENAME=={fname}")
    quit()
for line in fhandle:
    uline = line.upper()
    print(uline.rstrip()) 