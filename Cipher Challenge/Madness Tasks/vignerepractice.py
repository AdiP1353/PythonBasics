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
def decryption(ciphertext: str,key: str) -> str:
    ciphertext = ciphertext.upper()
    key = key.upper()
    plaintext = ''
    for i in range(len(ciphertext)):
        c = ALPHABET.index(ciphertext[i])
        k = ALPHABET.index(key[i%len(key)])
        p = (c - k) % 26
        plaintext += ALPHABET[p]
    return plaintext.lower()

print(decryption("PREGMPHTOLA","idiot"))




