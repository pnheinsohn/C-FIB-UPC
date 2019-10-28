import base64
import hashlib
from random import choice
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


ASCII = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

def open_file(path="files/2019_09_25_17_01_52_paul.heinsohn.puerta_trasera.enc"):
    with open(f"{path}", 'rb') as f:
        return f.read()

def save_file(path, decrypted):
    with open(path, 'wb') as f:
        f.write(decrypted)
    print(f"Succesful completion: {path} has been created")

class Keygen():

    def __init__(self):
        self.H = hashlib.sha256(self._pre_master_key()).digest()
        self.key = self.H[:16]
        self.iv =  self.H[16:]

    def _single_key(self):
        ascii_chars = ""
        while len(ascii_chars) != 16:
            char = choice(ASCII)
            if char not in ascii_chars:
                ascii_chars += f"{char}" * 8
        return ascii_chars

    def _pre_master_key(self):
        res = self._single_key()
        for _ in range(7): res = ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(res, self._single_key()))
        return res.encode()

    def print_key(self):
        print(f'''
        * Key *
            - Key: {self.key}
            - Len: {len(self.key)}
        --------------------------------------------------------------
        * iv *
            - iv: {self.iv}
            - Len: {len(self.iv)}
        ''')

class AESCipher():

    def __init__(self, key, iv):
        self.key = key
        self.iv = iv

    def decrypt(self, enc):
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        return unpad(cipher.decrypt(enc), AES.block_size)


if __name__ == "__main__":
    keygen = Keygen()
    aes = AESCipher(keygen.key, keygen.iv)
    
    data = open_file()
    decrypted = aes.decrypt(data)

    save_file("decrypted.txt", decrypted)
