import requests
from config import headers
import re


def get_sign_token(uid):
    r = requests.get("http://wechat.bodimall.com/christmas/" + str(uid), headers=headers)
    sign = re.search('.+var sign = \'(.*?)\'', r.text).group(1)
    token = re.search('.+var token = \'(.*?)\'', r.text).group(1)
    return sign, token


def get_steal_params(uid):
    sign, token = get_sign_token(uid)
    return {'sign': sign, 'token': token, 'value': 1, 'id': uid}
