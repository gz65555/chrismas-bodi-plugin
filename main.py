from random import randrange
from steal_and_pick import steal_and_pick_one
import time


def fuck_steal():
    uid = randrange(500, 20000)
    while True:
        if not steal_and_pick_one(uid):
            break
        interval = float(randrange(1, 8)) / 10
        time.sleep(interval)
    ss = randrange(2, 100)
    print()
    print("wait " + str(ss) + " seconds")
    print()
    time.sleep(ss)
    try:
        fuck_steal()
    finally:
        fuck_steal()
