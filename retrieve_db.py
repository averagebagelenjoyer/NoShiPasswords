# hello. if you're reading this uh... i added notes for your sake to read my spaghetti code.

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import json
import pyperclip # clipboard stuff
import configparser # important for the memes ALSO required for buffer
from pwinput import pwinput # it's like `getpass` but better
import _passwordlib as passwordLib # internal password lib which i only barely understand
import time

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
        decrypted_passwords = json.loads(passwordLib.decrypt(master, encrypted_data, salt))
        break
    except Exception as e:
        print("ERROR: Failed to decrypt most likely due to incorrect password")

passwords = []

# this prints out all the passwords (the passwords are censored with stars)
for i, (key, value) in enumerate(decrypted_passwords.items(), start=1):
    passwords.append(value)
    print(f"[{i}] {key}: {"*"*len(value)}")

# this lets you select the password you want
try:
    while True:
        entry = input("Copy Password (Or `Ctrl+C` to exit): ")
        try:
            pyperclip.copy(passwords[int(entry)-1])
            if config.getboolean("general", "clipboard_buffer", fallback=False):
                time.sleep(1)
                pyperclip.copy("Buffer")
            print("Copied to clipboard")
        except ValueError:
            print("ERROR: Not an integer")
        except IndexError:
            print("ERROR: Out of range")
except KeyboardInterrupt:
    pass
