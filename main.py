from random import randrange
from steal_and_pick import steal_and_pick_one
from get_sign import get_steal_params
import time


def fuck_steal():
    uid = randrange(500, 20000)
    payload = get_steal_params(uid)
    while True:
        if not steal_and_pick_one(payload):
            break
        # interval = float(randrange(1, 8)) / 10
        interval = float(randrange(1, 8)) / 10
        time.sleep(interval)
    ss = randrange(2, 10)
    print()
    print("wait " + str(ss) + " seconds")
    print()
    time.sleep(ss)
    try:
        fuck_steal()
    finally:
        fuck_steal()

fuck_steal()
