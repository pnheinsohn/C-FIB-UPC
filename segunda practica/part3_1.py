####################
##  Parte N°3.1   ##
####################

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad


BS = AES.block_size

def open_file(path="files/2019_09_25_17_01_52_paul.heinsohn", ext="enc"):
    with open(f"{path}.{ext}", 'rb') as f:
        return f.read()

def save_file(path, data):
    with open(path, "wb") as f:
        f.write(data)
    print(f"Successful completion: {path} has been created")

class AESCipher:

    def __init__(self, key):
        self.key = key

    def decrypt(self, enc):
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        # return cipher.decrypt(enc[16:])
        return unpad(cipher.decrypt(enc[16:]), BS)


if __name__ == "__main__":
    # bin_key = open_file(ext="key")
    bin_key = open_file(path="files/2019_09_25_17_02_54_alex.valls", ext="key")
    aes_crypt = AESCipher(bin_key)

    # bin_msg = open_file()
    bin_msg = open_file(path="files/2019_09_25_17_02_54_alex.valls")
    decrypted = aes_crypt.decrypt(bin_msg)
    
    # save_file("output/decrypted_paul.jpeg", decrypted)
    save_file("output/decrypted_alex.jpeg", decrypted)
