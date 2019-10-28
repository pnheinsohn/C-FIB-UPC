# Código hecho por pnheinsohn para ser replicado por otr@ alumn@

import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

## Part 3.1

# Open Key
file_in = open("2019_09_25_17_01_14_mariana.cardozo.key", 'rb')
key = file_in.read()
file_in.close()

# Open Crypted File
file_in = open("2019_09_25_17_01_14_mariana.cardozo.enc", 'rb')
iv = file_in.read(16)
data = file_in.read()
file_in.close()

cipher = AES.new(key, AES.MODE_CBC, iv)
try:
    decrypted = unpad(cipher.decrypt(data), AES.block_size) 
except ValueError as err:
    # Don't know why unpad throws Error
    print(err)
    decrypted = cipher.decrypt(data)
finally:
    # Save Decrypted File
    file_out = open("2019_09_25_17_01_14_mariana.cardozo", 'wb')  # Don't know the extension to open it
    file_out.write(decrypted)
    file_out.close()

print("Done Part 3.1")
print("Starting Part 3.2...")

## Part 3.2

ASCII = "".join([chr(num) for num in range(256)])
file_in = open("2019_09_25_17_01_14_mariana.cardozo.puerta_trasera.enc", 'rb')
data = file_in.read()
file_in.close()

counter = 0
ended = False
for char in ASCII:
    for char2 in ASCII:
        preMasterKey = "{}{}".format(char * 8, char2 * 8).encode()
        H = hashlib.sha256(preMasterKey).digest()
        key = H[:16]
        iv = H[16:]
        try:
            cipher = AES.new(key, AES.MODE_CBC, iv)
            decrypted = unpad(cipher.decrypt(data), AES.block_size)
        except ValueError:
            pass
        else:
            if counter == 800:  # En el 800 se usa la clave correcta
                file_out = open(f"2019_09_25_17_01_14_mariana.cardoso.puerta_trasera.mp4", "wb")
                file_out.write(decrypted)
                file_out.close()
                ended = True
                break
        finally:
            counter += 1
    if ended:
        break

print("Done Part 3.2")
