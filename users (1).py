import json
import os

file = "data/users.json"
os.makedirs("data", exist_ok=True)


def load():
    if not os.path.exists(file):
        return {}
    with open(file, "r") as f:
        return json.load(f)


def save(data):
    with open(file, "w") as f:
        json.dump(data, f)


def add_user(u, pw, rl):
    d = load()
    if u in d:
        return False
    d[u] = {"pw": pw, "rl": rl}
    save(d)
    return True


def login(u, pw):
    d = load()
    if u in d and d[u]["pw"] == pw:
        return d[u]
    return None


def get(u):
    d = load()
    return d.get(u)