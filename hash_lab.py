import hashlib

mystring = input('Enter string to hash: ')

hash_obj = hashlib.md5(mystring.encode())
print("Hash-code using md5:    ", hash_obj.hexdigest())

hash_obj = hashlib.sha1(mystring.encode())
print("Hash-code using sha1:   ", hash_obj.hexdigest())

hash_obj = hashlib.sha224(mystring.encode())
print("Hash-code using sha224: ", hash_obj.hexdigest())

hash_obj = hashlib.sha256(mystring.encode())
print("Hash-code using sha256: ", hash_obj.hexdigest())

hash_obj = hashlib.sha512(mystring.encode())
print("Hash-code using sha512: ", hash_obj.hexdigest())

BLOCK_SIZE = 2**20
with open('zayava.docx', 'rb') as inf:
    hash_obj = hashlib.sha1()
    while True:
        data = inf.read(BLOCK_SIZE)
        if not data:
            break
        hash_obj.update(data)

print("\n")
print("Hash-code for docx file: ",hash_obj.hexdigest())

'''''
with open('zayavaa.txt', 'r') as inf:
    data = str(inf.readlines())
    #print(data)
    hash_obj = hashlib.sha1(data.encode())
print("\n")
print("Hash-code for txt file: ", hash_obj.hexdigest())'''

