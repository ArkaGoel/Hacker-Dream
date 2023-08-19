from simplecrypt import encrypt, decrypt
import hashlib
import sys
import os
op = sys.argv

if(len(op) == 1):
    print("Welcome to the Hacker's Dream!\n")
    print("██╗░░██╗░█████╗░░█████╗░██╗░░██╗███████╗██████╗░██╗░██████╗  ██████╗░██████╗░███████╗░█████╗░███╗░░░███╗")
    print("██║░░██║██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗╚█║██╔════╝  ██╔══██╗██╔══██╗██╔════╝██╔══██╗████╗░████║")
    print("███████║███████║██║░░╚═╝█████═╝░█████╗░░██████╔╝░╚╝╚█████╗░  ██║░░██║██████╔╝█████╗░░███████║██╔████╔██║")
    print("██╔══██║██╔══██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗░░░░╚═══██╗  ██║░░██║██╔══██╗██╔══╝░░██╔══██║██║╚██╔╝██║")
    print("██║░░██║██║░░██║╚█████╔╝██║░╚██╗███████╗██║░░██║░░░██████╔╝  ██████╔╝██║░░██║███████╗██║░░██║██║░╚═╝░██║")
    print("╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝░░░╚═════╝░  ╚═════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝")
    print("Please type python main.py -h for commands")
    sys.exit()
elif(len(op) > 1):
    del op[0]
    for i in range(len(op)):
        val = op[i]
        if(val == "-e"):
            key = input("Enter a desired password: ")
            val = input("Provide text to encrypt: ")
            val_en = encrypt(key,  val)
            hexa = val_en.hex()
            print("Encrypted Value: " + str(hexa))
            print("Process done")
            sys.exit()
        elif(val == "-d"):
            try:
                val = input("Provide text to decrypt: ")
                key = input("Enter the Password: ")
                dec = bytes.fromhex(val)
                decr = decrypt(key, dec)
                deco = decr.decode('utf-8')
                print("Decrypted Value: " + deco)
                print("Process Finished")
                sys.exit()
            except Exception:
                print("Wrong Password! Terminating Program")
                sys.exit()
        elif(val == '-h'):
            print("Welcome to Hacking tool\n Made by Arka Goel")
            print("Usage: [-d] = decrypt, [-e] = encrypt, [-r] = ransomware documentation [-h] = help, [-m] = md5, [-s] = sha256, [-ef] = encrypt files, [-df] = decrypt files, [-de] = dehash functions")
            print("Don't try to use combinations because some processes may make the program unfuctional")
        elif(val == "-m"):
            raw = input("Provide Text to be hashed: ")
            md = hashlib.md5(raw.encode())
            text = md.hexdigest()
            print("MD5 Hash: " + str(text))
        elif(val == "-s"):
            raw = input("Provide Text to be hashed: ")
            sha = hashlib.sha256(raw.encode())
            text = sha.hexdigest()
            print("SHA256 Hash: " + text)
        elif(val == "-ef"):
            file_path = input("Provide File Path (NOTE: The file should be in the same folder as the program): ")
            passphrase = input("Enter Secure Password: ")
            print("Hang Tight! Processing Encryption")
            file_p = os.path.basename(file_path)
            file_op = open(file_p, 'r')
            file_text = file_op.read()
            file_data = encrypt(passphrase, file_text)
            file_data_hex = file_data.hex()
            file_wr = open(file_path, 'w')
            file_wr.write(file_data_hex)
            print("Encryption Done! Check the file.")
        elif(val == "-df"):
            file_path = input("Provide File Path (NOTE: The file should be in the same folder as the program): ")
            passphrase = input("Enter Secure Password: ")
            print("Hang Tight! Processing Decryption")
            file_p = os.path.basename(file_path)
            file_op = open(file_p, 'r')
            file_text = file_op.read()
            file_bytes = bytes.fromhex(file_text)
            try:
                file_data_decrypt = decrypt(passphrase, file_bytes)
                file_decode = file_data_decrypt.decode('utf-8')
                file_wr = open(file_path, 'w')
                file_wr.write(file_decode)
                print("Decryption Done! Check the file.")
            except Exception:
                print("Wrong Password, Terminating program!")
                sys.exit()
        elif(val == "-r"):
            print("NOTE: The file Provided here is a test ransomware file to learn how ransomware works and not intended for any malicious purposes this is purely for educational purposes\n")
            print("WARNING: Do not use these file in under any circumstances in your desktop or an important folder as it is a test program and may damage your files parmanently. Run this script on a sepereate test folder. It is a humble request\n")
            print("If you can't get your files back then the default passphrase for the decryption of files is Hacked@H1, but you may edit the password with your preferences in the ransomware file\n")
            print("Last but not Least: Use this with care to your computer NEVER run this file on root folder as it will destroy your system")