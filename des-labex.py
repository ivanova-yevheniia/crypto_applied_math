import des

ddd = des.DES()
cipher_hex = '85 E8 13 54 0F 0A B4 05'
key_hex = '13 34 57 79 9B BC DF F1'
decrypt_hex = '01 23 45 67 89 AB CD EF'

decrypt_txt = des.DECRYPT(key_hex, cipher_hex)
print("Deciphered (hex): {0}".format(decrypt_txt))