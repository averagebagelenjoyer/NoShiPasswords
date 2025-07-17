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

# this gets the path to the database you want to create
while True:
    file = input("Database (Ex: `passwords.json.enc`): ")
    if not os.path.exists(file):
        break
    print("ERROR: Invalid path")

# this gets your master password. twice in case of typos
while True:
    master = pwinput("Master Password: ")
    verify = pwinput("Verify Password: ")
    if master == verify:
        break
    print("ERROR: Passwords do not match")

passwords = {}

# this adds the base passwords you want in the database
try:
    while True:
        nickname = input("Password Nickname (Or `Ctrl+C` to finish): ")
        while True:
            password = pwinput("Password: ")
            verify   = pwinput("Verify Password: ")
            if password == verify:
                break
            print("ERROR: Passwords do not match")
        passwords[nickname] = password

# this saves the passwords
except KeyboardInterrupt:
    for key, value in passwords.items():
        if value != "":
            passwords[key] = value
    encrypted, salt = passwordLib.encrypt(master, json.dumps(passwords))
    wrapper = {
        "salt": salt,
        "data": encrypted
    }
    with open(file, "w") as f:
        json.dump(wrapper, f, indent=4)
    print(f"\n\nSuccessfully created `{file}`.")
