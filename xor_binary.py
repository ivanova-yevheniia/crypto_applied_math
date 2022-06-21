import random

ENCODING = 'cp866'

def convert_to_bin(line):
    return ' '.join(format(x, "08b") for x in line)

def key_create(message_b):
    random.seed(8)
    return bytes(random.randint(0, 255) for i in range(len(message_b)))

def xor_encode(message):
    message_b = message.encode(ENCODING)

    key_gamma_b = key_create(message_b)
    print('Key gamma:  ', ' '.join(format(x, "03d") for x in key_gamma_b))

    message_bin = convert_to_bin(message_b)
    print(f'Message b:   {message_bin}')

    key_gamma_bin = convert_to_bin(key_gamma_b)
    print(f'Key gamma b: {key_gamma_bin}')

    encoded_b = bytes(x ^ y for x, y in zip(message_b, key_gamma_b))
    print(f'Ciphertext:  {convert_to_bin(encoded_b)}')

def xor_decode(gamma_b, cipher_b):
    gamma_int = [int(x, 2) for x in gamma_b.split()]
    print("Key_gamma  ", gamma_int)

    ciphertext_int = [int(x, 2) for x in cipher_b.split()]
    print("Ciphertext ", ciphertext_int)

    message_b = bytes([x ^ y for x, y in zip(ciphertext_int, gamma_int)])
    print("Message:   ", message_b.decode(ENCODING))

    print("Message b: ", convert_to_bin(message_b))

if __name__ == "__main__":
    message = 'BLACKSABBATH'
    print('Message:    ', message)
    xor_encode(message)
    print("\n")
    xor_decode('01110100 10111101 11000000 01000000 01100010 00010110 00101011 01000110 01111110 01101011 11001101',
               '00100000 11010010 10101101 01100000 00101010 01111001 01000111 00101010 00011111 00000101 10101001')