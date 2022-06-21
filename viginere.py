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
    x = (ord(plaintext[i]) + ord(key[i])) % 26
    x += ord('A')
    cipher.append(chr(x))
  return("" .join(cipher))


def decryption(cipher, key):
  plaintext = []
  for i in range(len(cipher)):
    x = (ord(cipher[i]) - ord(key[i]) + 26) % 26
    x += ord('A')
    plaintext.append(chr(x))
  return("" .join(plaintext))


if __name__ == "__main__":
  plaintext = input("Enter the message: ")
  key = input("Enter the key: ")
  cipher = encryption(plaintext, key)
  print("Encrypted message: ", cipher)
  print("Decrypted message: ", decryption(cipher, key))
