text = "X-DSPAM-Confidence:    0.8475"
colon = text.find(":")
unstrip = text[colon+1: ]
striptext = unstrip.strip()
print(float(striptext))