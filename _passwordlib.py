import base64
import os
import configparser
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet

# uhhhhhhhhhhhh. if it ain't broke don't fix it.
# i have no clue what this does tbh. i know it's safe.

config = configparser.ConfigParser()
config.read("config.ini")

iterations = config.getint("encryption", "iterations", fallback=100_000)

def derive_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=iterations,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())
    return base64.urlsafe_b64encode(key)

def encrypt(master_password: str, plaintext_password: str) -> tuple[str, str]:
    salt = os.urandom(16)
    key = derive_key(master_password, salt)
    fernet = Fernet(key)
    encrypted = fernet.encrypt(plaintext_password.encode())
    return encrypted.decode(), base64.urlsafe_b64encode(salt).decode()

def decrypt(master_password: str, encrypted_password: str, encoded_salt: str) -> str:
    salt = base64.urlsafe_b64decode(encoded_salt.encode())
    key = derive_key(master_password, salt)
    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted_password.encode())
    return decrypted.decode()