import json
import os
import time
import hashlib

file = "data/block.json"
os.makedirs("data", exist_ok=True)


def load():
    if not os.path.exists(file):
        return []
    with open(file, "r") as f:
        return json.load(f)


def save(d):
    with open(file, "w") as f:
        json.dump(d, f)


def make_hash(b):
    txt = str(b["no"]) + b["prev"] + b["h"] + b["i"] + b["s"] + str(b["t"])
    return hashlib.sha256(txt.encode()).hexdigest()


def add(h, i, s):
    d = load()
    if d == []:
        p = "first"
    else:
        p = d[-1]["hash"]

    nb = {
        "no": len(d),
        "prev": p,
        "h": h,
        "i": i,
        "s": s,
        "t": int(time.time())
    }

    nb["hash"] = make_hash(nb)
    d.append(nb)
    save(d)
    return nb


def find(h):
    d = load()
    r = []
    for b in d:
        if b["h"] == h:
            r.append(b)
    return r 