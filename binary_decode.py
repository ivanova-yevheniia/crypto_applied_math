#-*- coding: utf-8 -*-
ENCODING = 'cp866'

gamma_binary = \
    '01110100 10111101 11000000 01000000 01100010 00010110 00101011 01000110 01111110 01101011 11001101 00001111'
ciphertext_binary = \
    '00110110 11110001 10000001 00000011 00101001 01000101 01101010 00000100 00111100 00101010 10011001 01000111'

gamma_int = [int(x, 2) for x in gamma_binary.split()]
print("Key_gamma  (int): ", gamma_int)

ciphertext_int = [int(x, 2) for x in ciphertext_binary.split()]
print("Ciphertext (int): ", ciphertext_int)
            
message_b = bytes(x ^ y for x, y in zip(ciphertext_int, gamma_int))

print("Message: ", message_b.decode(ENCODING))



