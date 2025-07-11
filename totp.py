import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from pwinput import pwinput # it's like `getpass` but better
import argparse # required for command line and GUI

# all of this is required for the TOTP
import base64
import hashlib
import hmac
import struct
import time

import sys

parser = argparse.ArgumentParser(description="Example: greet user with optional shout")
parser.add_argument("-c", "--commandLine", action="store_true", help="This must be set if used in the command line")
parser.add_argument("-S", "--secret", help="TOTP secret")

args = parser.parse_args()

def get_totp_token(secret, interval=30, digits=6):
    try:
        key = base64.b32decode(secret.upper())
        counter = int(time.time()) // interval
        msg = struct.pack(">Q", counter)
        h = hmac.new(key, msg, hashlib.sha1).digest()
        o = h[19] & 15
        token = (struct.unpack(">I", h[o:o+4])[0] & 0x7fffffff) % (10 ** digits)
        return str(token).zfill(digits)
    except:
        return False

if args.commandLine:
    token = get_totp_token(args.secret)

    if token:
        print(token)
        sys.exit(0)
    else:
        print("invalid secret", sys.stderr)
        sys.exit(2)

while True:
    secret = pwinput("TOTP secret (Leave empty to exit): ")

    if not secret:
        sys.exit(0)

    token = get_totp_token(secret)

    if token:
        print("TOTP code: ", token)
    else:
        print("Invalid TOTP secret")
