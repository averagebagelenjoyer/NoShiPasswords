# hello. if you're reading this uh... i added notes for your sake to read my spaghetti code.

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import json
import configparser # important for the memes
from pwinput import pwinput # it's like `getpass` but better
import _passwordlib as passwordLib # internal password lib which i only barely understand

# uh- ok this feature is genuinely just a joke
config = configparser.ConfigParser()
config.read("config.ini")

if config.getboolean("general", "gui", fallback=False):
    print("ERROR: GUI is forbidden. I am a Linux user")

# this gets the database you want to retrieve passwords from
while True:
    file = input("Database (Ex: `passwords.json.enc`): ")
    if os.path.exists(file):
        break
    else:
        print("ERROR: Invalid path")

# this uh... oh yeah loads the json i nearly forgot
with open(file, "r") as f:
    passwords = json.load(f)

salt = passwords["salt"]
encrypted_data = passwords["data"]

# this gets your master password
while True:
    master = pwinput("Master Password: ")
    try:
        passwords = json.loads(passwordLib.decrypt(master, encrypted_data, salt))
        break
    except Exception as e:
        print("ERROR: Failed to decrypt most likely due to incorrect password")

# this prints out all the passwords (the passwords are censored with stars)
for i, (key, value) in enumerate(passwords.items(), start=1):
    print(f"{key}: {"*"*len(value)}")

# this lets you update the passwords
try:
    while True:
        nickname = input("Password Nickname (Or `Ctrl+C` to finish): ")
        while True:
            password = pwinput("Password (Leave empty to delete): ")
            if password == "":
                break
            verify   = pwinput("Verify Password: ")
            if password == verify:
                break
            print("ERROR: Passwords do not match")
        if password:
            passwords[nickname] = password
        else:
            del passwords[nickname]

# this updates the passwords
except KeyboardInterrupt:
    encrypted, salt = passwordLib.encrypt(master, json.dumps(passwords))
    wrapper = {
        "salt": salt,
        "data": encrypted
    }
    with open(file, "w") as f:
        json.dump(wrapper, f, indent=4)
    print(f"\n\nSuccessfully updated `{file}`.")