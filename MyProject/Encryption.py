from Crypto.Cipher import AES
import base64


class Encryption(object):

    # constructor
    def __init__(self, key, enc_type="AES", block=16):
        self.__cipher = AES.new(key)
        self.encrypt_type = enc_type
        self.block_size = block
        self.padding = '{'

    # add padding to message to get right block size
    def add_padding(self, data):
        """
        :param data: message to pad
        :return: padded data according to self.block_size
        """
        num = self.block_size - len(data) % self.block_size
        return data + num * self.padding

    # encryption function
    def encryptAES(self, data):
        """
        Adds padding to data, encrypts it with AES, and encodes with base64
        (also deals with a case of '/' in string)
        :param data: message to encrypt
        :return: padded, encrypted, encoded data
        """
        padded = self.add_padding(data)
        encrypted = self.__cipher.encrypt(padded)
        encoded = base64.b64encode(encrypted)
        final = self.remove_slash(encoded)
        return final

    # decryption function
    def decryptAES(self, encoded):
        """
        Decodes message with base64, decrypts with AES, and removes padding
        (also deals with a case of '/' in string)
        :param encoded: message to encrypt
        :return: the original message
        """
        correct = self.add_slash_again(encoded)
        decoded = base64.b64decode(correct)
        decrypted = self.__cipher.decrypt(decoded)
        no_padding = decrypted.rstrip(self.padding)
        return no_padding

    # changes all '/' to '$'
    def remove_slash(self, data):
        """
        If '/' is in the encrypted string, it is viewed as part of the URL,
        which causes a problem in defining the correct page path.
        This function solves the problem by changing all '/' to '$'.
        :param data: encrypted message
        :return: data with all '/' changed to '$'
        """
        while '/' in data:
            i = data.find('/')
            data = data[:i] + '$' + data[i+1:]
        return data

    # changes all '$' back to '/'
    def add_slash_again(self, data):
        """
        To properly decrypt a message, all '$' should be changed bac to '/'.
        Otherwise decryption won't return the original message.
        :param data: encrypted message
        :return: data with all '$' changed back to '/'
        """
        while '$' in data:
            i = data.find('$')
            data = data[:i] + '/' + data[i+1:]
        return data
