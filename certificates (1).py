import json
import os
import time
import hashlib
import blockchain_sim

file = "data/cert.json"
os.makedirs("data", exist_ok=True)


def load():
    if not os.path.exists(file):
        return {}
    with open(file, "r") as f:
        return json.load(f)


def save(d):
    with open(file, "w") as f:
        json.dump(d, f)


def make_hash(x):
    h = hashlib.sha256()
    h.update(x)
    return h.hexdigest()


def give(i, s, x, info):
    d = load()
    h = make_hash(x)
    cid = "c" + h[:6]

    new = {
        "id": cid,
        "i": i,
        "s": s,
        "h": h,
        "info": info,
        "t": int(time.time())
    }

    d[cid] = new
    save(d)

    blockchain_sim.add(h, i, s)

    return new


def get(cid):
    d = load()
    return d.get(cid)


def all_of(s):
    d = load()
    r = []
    for c in d.values():
        if c["s"] == s:
            r.append(c)
    return r