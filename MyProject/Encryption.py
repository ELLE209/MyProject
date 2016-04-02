from Crypto.Cipher import AES
import base64
import os


class Encryption(object):

    def __init__(self, key, enc_type="AES", block=16):
        self.cipher = AES.new(key)
        self.encrypt_type = enc_type
        self.block_size = block
        self.padding = '{'

    def add_padding(self, data):
        num = self.block_size - len(data) % self.block_size
        return data + num * self.padding

    def encryptAES(self, data):
        padded = self.add_padding(data)
        encrypted = self.cipher.encrypt(padded)
        encoded = base64.b64encode(encrypted)
        final = self.remove_slash(encoded)
        return final

    def decryptAES(self, encoded):
        correct = self.add_slash_again(encoded)
        decoded = base64.b64decode(correct)
        decrypted = self.cipher.decrypt(decoded)
        no_padding = decrypted.rstrip(self.padding)
        return no_padding

    def remove_slash(self, data):
        while '/' in data:
            i = data.find('/')
            data = data[:i] + '$' + data[i+1:]
        return data

    def add_slash_again(self, data):
        while '$' in data:
            i = data.find('$')
            data = data[:i] + '/' + data[i+1:]
        return data

'''
e = Encryption(b'Sixteen Byte Key')
enc = e.encryptAES('101')
print enc
print e.decryptAES(enc)
'''
