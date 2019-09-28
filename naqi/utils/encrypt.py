from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_v1_5
import hashlib
from naqi.settings import SLAT

def create_rsa_key():
    key = RSA.generate(2048)
    pri_key = key.export_key(pkcs=8)
    pub_key = key.publickey().exportKey()
    with open('./pri.key', 'wb') as f:
        f.write(pri_key)
    with open('./pub.pem', 'wb') as f:
        f.write(pub_key)

def generate_key():
    key = RSA.generate(2048)
    private_key = key.export_key(pkcs=8)
    return private_key.decode(), key.publickey().exportKey().decode()

def encrypt_data(public_key, data):
    cipher = RSA.import_key(public_key)
    recipient_key = PKCS1_v1_5.new(cipher)
    encrypt_data = recipient_key.encrypt(data)
    # hex_data = binascii.hexlify(encrypt_data).decode('utf-8')
    return encrypt_data

def decrypt_data(hex_data):
    pri_key = RSA.import_key(
        open('./pri.key').read(),
    )
    cipher = PKCS1_v1_5.new(pri_key)
    # en_data = binascii.unhexlify(hex_data.encode('utf-8'))
    data = cipher.decrypt(hex_data, None)
    return data

def SHA256(text):
    text = text + SLAT.encode('utf-8')
    hex = hashlib.sha256(text)
    return hex.hexdigest()
