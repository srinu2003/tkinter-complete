from os import getcwd
from os.path import isfile
from cryptography.fernet import Fernet

class KeyNotFoundError(FileNotFoundError):
    def __init__(self, *args: object) -> None:
        super().__init__('No key found in Dir: \''+args[0]+'\\\'')

    def __str__(self) -> str:
        return super().__str__()

def generate_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)

def load_key():
    if(not isfile('./key.key')):
        current_dir = getcwd()
        raise KeyNotFoundError((current_dir))
    
    with open('key.key', 'rb') as key_file:
        key = key_file.read()
    return key

def encrypt_message(message, key):
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message, key):
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)
    return decrypted_message.decode()
