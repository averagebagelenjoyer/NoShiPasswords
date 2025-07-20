# hello. if you're reading this uh... i added notes for your sake to read my spaghetti code.

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import re # required for error detection
import rstr # very very important for the password generation
import pyperclip # clipboard stuff
import configparser # important for the memes ALSO required for buffer
import time

# uh- ok this feature is genuinely just a joke
config = configparser.ConfigParser()
config.read("config.ini")

if config.getboolean("general", "gui", fallback=False):
    print("ERROR: GUI is forbidden. I am a Linux user")

print("This is a RegEx-based password generator. Prefix the RegEx with `!` to copy.")
try:
    while True:
        regex = input("RegEx (Or `Ctrl+C` to exit): ")

        try:
            if regex.startswith("!"):
                pyperclip.copy(rstr.xeger(regex[1:]))
                if config.getboolean("general", "clipboard_buffer", fallback=False):
                    time.sleep(1)
                    pyperclip.copy("Buffer")
                print("Copied to clipboard")
            else:
                print(rstr.xeger(regex))
        except re.PatternError:
            print("ERROR: Invalid RegEx")
        except ValueError:
            print("ERROR: Too long")
        except OverflowError:
            print("ERROR: Way too long")
except KeyboardInterrupt:
    pass
