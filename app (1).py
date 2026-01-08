from users import add_user, login
from certificates import give, all_of
from portfolio import show
from verifier import check
from security import enc, dec


def main():
    print("start demo...")

    add_user("inst1", "111", "inst")
    add_user("stud1", "222", "stud")

    inst = login("inst1", "111")

    txt = "certificate for stud1 blockchain"
    data = txt.encode()

    info = {"course": "bc", "grade": "A"}

    give(inst["rl"], "stud1", data, info)
    print("given cert ")

    print("portfolio:", show("stud1"))

    print("verify:", check(data, "stud1"))

    e = enc(data)
    print("enc:", e)

    d = dec(e)
    print("dec:", d.decode())

if __name__ == "__main__":
    main()