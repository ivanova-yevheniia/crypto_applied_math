
# LOWERCASE ENCRYPTION IMPLEMENTATION ONLY

OFFSET_LOWERCASE = 97

def keygenerate(plaintext, key):
  key = list(key)
  if len(plaintext) == len(key):
    return (key)
  else:
    for i in range(len(plaintext) - len(key)):
      key.append(key[i % len(key)])
  return ("".join(key))



def encryption(plaintext, key):
  cipher = []
  for i in range(len(plaintext)):
    x = (ord(plaintext[i]) + ord(key[i]) - 2*OFFSET_LOWERCASE) % 26
    cipher.append(chr(x + OFFSET_LOWERCASE))
  return("" .join(cipher))


def decryption(cipher, key):
  plaintext = []
  for i in range(len(cipher)):
    x = (ord(cipher[i]) - ord(key[i])) % 26
    plaintext.append(chr(x + OFFSET_LOWERCASE))
  return("" .join(plaintext))


if __name__ == "__main__":
  plaintext = input("Enter the message: ")
  keyword = input("Enter the keyword: ")
  key = keygenerate(plaintext, keyword)
  cipher = encryption(plaintext, key)
  print("Encrypted message: ", cipher)
  print("Decrypted message: ", decryption(cipher, key))
