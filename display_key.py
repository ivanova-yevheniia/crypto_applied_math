import rsa

with open('private_key_1024.pem', 'rb') as inf:
    priv_key = rsa.PrivateKey.load_pkcs1(inf.read())

print("n={} d={}".format(priv_key.n, priv_key.d))

with open('public_key_1024.pem', 'rb') as inf:
    public_key = rsa.PublicKey.load_pkcs1(inf.read())

print("n={} e={}".format(public_key.n, public_key.e))