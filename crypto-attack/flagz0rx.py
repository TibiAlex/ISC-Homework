#!/usr/bin/env python3
# Giff me za flag!

import os
import base64
from Crypto.Cipher import AES
from Crypto.Util import number

BLOCK_SIZE = 32
PADDING = b'\x00'
FLAG = os.getenv('FLAG')

def gen_params():
    q = number.getPrime(256)
    p = 2 * q + 1
    while not number.isPrime(p):
        q = number.getPrime(256)
        p = 2 * q + 1
    g = 2
    print(p, g)
    return (p, g)

def pad(s):
    return s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING 

def encrypt_aes(msg, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(msg)


if __name__ == "__main__":
    p, g = gen_params()
    my_priv = number.getPrime(512)
    my_pub = int(pow(g, my_priv, p))

    print("I chose: modulus=%i, generator=%i" % (p, g))
    print("My public key: ", my_pub)

    yours = int(input("Please give yours: "))

    shared = int(pow(yours, my_priv, p))
    key = shared.to_bytes((shared.bit_length() + 7) // 8, byteorder='big')[0:BLOCK_SIZE]
    msg = pad(str(FLAG).encode("ASCII"))
    c = encrypt_aes(msg, key)
    print("Here's your flag:")
    print(base64.encodebytes(c).decode("ASCII"))

