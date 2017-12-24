import requests
from get_sign import get_steal_params
from config import headers
import time
from random import randrange


# 5s


def steal_and_pick_one(payload):
    r = requests.get("http://wechat.bodimall.com/index/christmastree/steal", params=payload, headers=headers)
    uid = payload['id']
    code = r.json()['code']

    if code == 0:
        print('steal id: ' + str(uid) + ' 1 gift')
        interval = float(randrange(1, 2)) / 10
        time.sleep(interval)
        pickR = requests.get("http://wechat.bodimall.com/index/christmastree/pick?type=free_gift&value=1",
                            headers=headers)
        print(pickR.json())

        return True
    else:
        return False


def steal(uid):
    payload = get_steal_params(uid)

    def inner_steal():
        interval = float(randrange(1, 3)) / 10
        r = requests.get("http://wechat.bodimall.com/index/christmastree/steal", params=payload, headers=headers)
        code = r.json()['code']
        if code == 0:
            print('steal id: ' + str(uid) + ' 1 gift')
            time.sleep(interval)
            inner_steal()

    inner_steal()


def pick():
    def inner_pick():
        interval = float(randrange(1, 3)) / 10
        r = requests.get("http://wechat.bodimall.com/index/christmastree/pick?type=free_gift&value=1", headers=headers)
        code = r.json()['code']
        print(r.json())
        if code == 0:
            time.sleep(interval)
            inner_pick()

    inner_pick()


def steal_and_pick(uid):
    steal(uid)
    pick()