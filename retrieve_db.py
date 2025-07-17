# hello. if you're reading this uh... i added notes for your sake to read my spaghetti code.

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import json
import pyperclip # clipboard stuff
import configparser # important for the memes ALSO required for buffer
from pwinput import pwinput # it's like `getpass` but better
import _passwordlib as passwordLib # internal password lib which i only barely understand
import time
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("-S", "--simple", action="store_true", help="Used for GUI tools")

args = parser.parse_args()

# uh- ok this feature is genuinely just a joke
config = configparser.ConfigParser()
config.read("config.ini")

if config.getboolean("general", "gui", fallback=False) and not args.simple:
    print("ERROR: GUI is forbidden. I am a Linux user")

# this gets the database you want to retrieve passwords from
while True:
    file = input("0" if args.simple else "Database (Ex: `passwords.json.enc`): ")
    if os.path.exists(file):
        break
    else:
        if args.simple:
            print("invalid path", file=sys.stderr)
            sys.exit(2)
        print("ERROR: Invalid path")

# this uh... oh yeah loads the json i nearly forgot
with open(file, "r") as f:
    passwords = json.load(f)

salt = passwords["salt"]
encrypted_data = passwords["data"]

# this gets your master password
while True:
    master = input("1") if args.simple else pwinput("Master Password: ")
    try:
        decrypted_passwords = json.loads(passwordLib.decrypt(master, encrypted_data, salt))
        break
    except Exception as e:
        if args.simple:
            print("invalid passwd", file=sys.stderr)
            sys.exit(2)
        print("ERROR: Failed to decrypt most likely due to incorrect password")

passwords = []

# this prints out all the passwords (the passwords are censored with stars)
for i, (key, value) in enumerate(decrypted_passwords.items(), start=1):
    passwords.append(value)
    print(f'"{key}"{value}' if args.simple else f"[{i}] {key}: {"*"*len(value)}")

if args.simple: sys.exit(0)

# this lets you select the password you want
try:
    while True:
        entry = input("2" if args.simple else "Copy Password (Or `Ctrl+C` to exit): ")
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
