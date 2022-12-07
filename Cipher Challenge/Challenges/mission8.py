def split_by_index(ctext: str, n: int) -> int:
    ctext = ctext.replace(" ", "")
    ctext.upper()

    return ctext[::n] 
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
def remove_consecutive_indexes(input: str, start: int, end: int) -> str:
        cipher_text_list = list(input)
        for i in range((end - start) + 1):
            del cipher_text_list[start - 1::start]

        finallist = ''.join(cipher_text_list)
        return finallist
def split_string_every_n_blocks(input_string: str, blocklength: int) -> list:
    blocklength = int(blocklength)
    ciphertext = input_string
    list_out = []
    rangeofexecution = len(input_string) / blocklength
    rangeofexecution = int(rangeofexecution)
    
    for i in range(rangeofexecution):
        new_block = ciphertext[:blocklength]
        list_out.append(new_block)
        ciphertext = ciphertext.replace(new_block, '', 1)
        
    return list_out    
def subtract_key_length(input_string: str, sub_num: int) -> str:
    numbers = [
        ord(char) - 97 for char in input_string.lower()
    ]

    for i in range(len(numbers)):
        numbers[i] =numbers[i] - sub_num
        if numbers[i] < 0:
            numbers[i] = 26 + numbers[i]

    numbers = [
        chr(numbers[j] + 97) for j in range(len(numbers))
    ]

    final = ''.join(numbers)

    return final
def ic(self):
  num = 0.0
  den = 0.0
  for val in self.count.values():
    i = val
    num += i * (i - 1)
    den += i
  if (den == 0.0):
    return 0.0
  else:
    return num / ( den * (den - 1))


