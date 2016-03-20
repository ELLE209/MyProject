from Crypto.Cipher import AES
import base64
import os


class Encryption():

    def __init__(self, enc_type="AES", block=16):
        self.encrypt_type = enc_type
        self.block_size = block
        self.padding = '{'

    def run(self):  # , data, key):
        # one-liner to sufficiently pad the text to be encrypted
        pad = lambda s: s + (self.block_size - len(s) % self.block_size) * self.padding

        # one-liners to encrypt/encode and decrypt/decode a string
        # encrypt with AES, encode with base64
        EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
        DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(self.padding)

        # generate a random secret key
        secret = os.urandom(self.block_size)

        # create a cipher object using the random secret
        cipher = AES.new(secret)

        # encode a string
        encoded = EncodeAES(cipher, 'password')
        print 'Encrypted string:', encoded

        # decode the encoded string
        decoded = DecodeAES(cipher, encoded)
        print 'Decrypted string:', decoded
        #encrypted = data, key
        #return encrypted

e = Encryption()
e.run()