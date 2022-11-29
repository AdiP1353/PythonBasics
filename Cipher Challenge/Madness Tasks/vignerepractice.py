ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encryption(plaintext, key):
    ciphertext = ''
    for i in range(len(plaintext)):
        p = ALPHABET.index(plaintext[i])
        k = ALPHABET.index(key[i%len(key)])
        c = (p + k) % 26
        ciphertext += ALPHABET.index[c]
         
encryption('geeksforgeeks', 'ayush')