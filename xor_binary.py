def xor_key_plaintext(plaintext: str, key: bytes):
    spl_key = key.split(" ")
    txt = []
    for a, b in zip(plaintext, spl_key):
        txt.append(ord(a) ^ int(b))
    return txt

def convert_to_bin(line):
    return ' '.join(format(x, "08b") for x in line)

result = xor_key_plaintext("BLACKSABBATH", "116 189 192 064 098 022 043 070 126 107 205 015")
print(convert_to_bin(result))

print(convert_to_bin("Tom Holland"))

