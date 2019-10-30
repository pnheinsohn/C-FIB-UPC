###################
##  Parte N°3.2  ##
###################

import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad


ASCII = ''.join([chr(i) for i in range(256)])

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
    print(f"Successful completion: {path} has been created")

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
            aes = AESCipher(H[:16], H[16:])
            decrypted = aes.decrypt(data)
        except ValueError:
            pass
        except StopIteration:
            break
        else:
            id_ = next(id_generator)
            # if id_ == 92:  # N°92 from 0 to 278
            #     save_file(f"output/decrypted_paul.puerta_trasera.mp4", decrypted)
            #     break
            if id_ == 21:  # N°21 from 0 to 279
                save_file(f"output/decrypted_alex.puerta_trasera.mp4", decrypted)
                break
