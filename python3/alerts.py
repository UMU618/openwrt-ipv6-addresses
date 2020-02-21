#!/usr/bin/env python3
# Copyright 2020 UMU618.
#
# Authors: UMU618 <umu618@hotmail.com>
#
import base64
import hashlib
import hmac
import json
import ssl
import time
import urllib.request
import urllib.parse

URL_ROOT = 'https://oapi.dingtalk.com'


def get_sign(timestamp, secret):
    to_sign = str(timestamp) + '\n' + secret
    h = hmac.new(secret.encode('utf-8'), to_sign.encode('utf-8'),
                 digestmod=hashlib.sha256).digest()
    return base64.b64encode(h)


def send_dingtalk(token, secret, text):
    if not token or not text:
      print('Message:', text)
      return True

    url = URL_ROOT+'/robot/send?access_token='+token
    if secret:
      timestamp = round(time.time() * 1000)
      sign = get_sign(timestamp, secret)
      url += '&timestamp='+str(timestamp)+'&sign='+urllib.parse.quote(sign)
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    body = bytes(json.dumps(
        {'msgtype': 'text', 'text': {'content': text}}), 'utf-8')
    try:
        req = urllib.request.Request(url, data=body, headers=headers)
        response = urllib.request.urlopen(
            req, context=ssl._create_unverified_context())
        if response.code != 200:
            print('fail to send dingtalk, status =', response.code)
            return False
        jo = json.loads(response.read())
        if jo['errcode'] == 0:
            print('Message sent:', text)
        else:
            print('fail to send dingtalk:', jo)
            return False
        return True
    except Exception as err:
        print('fail to send dingtalk, exception:', err)
        return False


if __name__ == '__main__':
    print('URL_ROOT:', URL_ROOT)
    secret = 'UMU'
    timestamp = 618
    sign = get_sign(timestamp, secret)
    print('secret:', secret)
    print('timestamp:', timestamp)
    print('sign:', sign.decode('utf-8'))
