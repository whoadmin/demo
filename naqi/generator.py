from Cryptodome.PublicKey import RSA

def create_rsa_key():
    key = RSA.generate(2048)
    pri_key = key.export_key(pkcs=8)
    pub_key = key.publickey().exportKey()
    with open('./pri.key', 'wb') as f:
        f.write(pri_key)
    with open('./pub.pem', 'wb') as f:
        f.write(pub_key)

create_rsa_key()