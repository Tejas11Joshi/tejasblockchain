from cryptography.fernet import Fernet
import os

key_file = "data/key.txt"
os.makedirs("data", exist_ok=True)


def make_key():
    k = Fernet.generate_key()
    with open(key_file, "wb") as f:
        f.write(k)
    return k


def read_key():
    if not os.path.exists(key_file):
        return make_key()
    return open(key_file, "rb").read()


def enc(x):
    k = read_key()
    f = Fernet(k)
    return f.encrypt(x)


def dec(x):
    k = read_key()
    f = Fernet(k)
    try:
        return f.decrypt(x)
    except:
        return None