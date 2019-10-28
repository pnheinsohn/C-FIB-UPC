from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad


# Open Key
file_in = open("2019_09_25_17_01_14_mariana.cardozo.key", 'rb')
key = file_in.read()
file_in.close()

# Open Crypted File
file_in = open("2019_09_25_17_01_14_mariana.cardozo.enc", 'rb')
iv = file_in.read(16)
cipher = AES.new(key, AES.MODE_CBC, iv)
# decrypted = cipher.decrypt(file_in.read())
# Don't know why unpad throws Error
decrypted = unpad(cipher.decrypt(file_in.read()), AES.block_size) 
file_in.close()

# Save Decrypted File
file_out = open("decrypted.txt", 'wb')  # Don't know the extension to open it
file_out.write(decrypted)
file_out.close()

print("Done")