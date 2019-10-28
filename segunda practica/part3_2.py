import base64
import hashlib
from random import choice
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


ASCII = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789#$%&/()=¿?¡!*~^{ }[]-_:;.,<>+\"'|°¬´¨"

def gen_key():
    for a in ASCII:
        for b in ASCII:
            yield f"{a * 8}{b * 8}"

def gen_id():
    id_ = 0
    while True:
        yield id_
        id_ += 1

def open_file(path="files/2019_09_25_17_01_52_paul.heinsohn.puerta_trasera.enc"):
    with open(f"{path}", 'rb') as f:
        return f.read()

def save_file(path, decrypted):
    with open(path, 'wb') as f:
        f.write(decrypted)
    print(f"Succesful completion: {path} has been created")

class AESCipher:

    def __init__(self, key, iv):
        self.key = key
        self.iv = iv

    def decrypt(self, enc):
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        return unpad(cipher.decrypt(enc), AES.block_size)

if __name__ == "__main__":
    # data = open_file()
    data = open_file("files/2019_09_25_17_02_54_alex.valls.puerta_trasera.enc")
    key_generator = gen_key()
    id_generator = gen_id()

    while True:
        try:
            H = hashlib.sha256(next(key_generator).encode()).digest()
            key = H[:16]
            iv = H[16:]
            aes = AESCipher(key, iv)
            decrypted = aes.decrypt(data)
        except ValueError:
            pass
        except StopIteration:
            break
        else:
            id__ = next(id_generator)
            # save_file(f"new/decrypted_paul.puerta_trasera_{id__}", decrypted)
            save_file(f"new/decrypted_alex.puerta_trasera_{id__}", decrypted)
