
	#fout.write(' '.join(line.split()))
 
import re
	
fin = open("mycorpus.txt", "rt")
fout = open("finalcorpus.txt", "wt")

for line in fin:
	fout.write(re.sub('\s+',' ',line))
	
fin.close()
fout.close()




# import re

# regex = re.compile('[^a-zA-Z \n]')
# corpus = open("browncorpus.txt","r").read()
# bling = (regex.sub("", corpus))

# open("mycorpus.txt","w").write(bling)
# print("done")
#Out: 'abdE'