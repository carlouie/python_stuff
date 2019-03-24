""""
Dictionary attack
Description: Finds the password for the given hash within
a list of passwords
"""


import hashlib

flag = 0

pass_hash = input("Enter MD5 Hash: ")
word_list = input("File Name: ")

try:
    pass_file = open(word_list, "r")
except:
    print("No file found")
    quit() #closes program so user can retry file entry
    
#Type logic to compare word_file

for word in pass_file:
    
    enc_wrd = word.encode('utf-8') #when trying to hash any string in python; certain type of encoding
    digest = hashlib.md5(enc_wrd.strip()).hexdigest()
    #hexadecimal format (hexdigest)

    if digest == pass_hash:
        print("Password Found")
        print("Password is: " + word)
        flag = 1
        break
    
if flag == 0:
    print("Password/Passphrase is not in the list")
