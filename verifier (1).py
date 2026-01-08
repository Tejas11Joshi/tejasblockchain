from certificates import make_hash
import blockchain_sim


def check(x, s):
    h = make_hash(x)
    b = blockchain_sim.find(h)
    for i in b:
        if i["s"] == s:
            return True
    return False