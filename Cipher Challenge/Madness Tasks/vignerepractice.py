ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encryption(plaintext: str, key: str) -> str:
    plaintext = plaintext.upper()
    key = key.upper()
    ciphertext = ''
    for i in range(len(plaintext)):
        p = ALPHABET.index(plaintext[i])
        k = ALPHABET.index(key[i%len(key)])
        c = (p + k) % 26
        ciphertext += ALPHABET[c]
    return ciphertext    
         
print(encryption('geeksforgeeks', 'ayush'))