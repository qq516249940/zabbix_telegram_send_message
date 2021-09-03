#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
import json
import sys
import os
 

headers = {'Content-Type': 'application/json;charset=utf-8'}
api_url = " https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxx"   #这个是webhook地址，修改为你的即可。

"""
使用
python3 wechat_bot.py 你好，测试信息
zabbix脚本参数只需 {ALERT.MESSAGE}
"""


def msg(text):
    json_text= {
     "msgtype": "text",
        "text": {
            "content": text
        },
    }
    print(requests.post(api_url,json.dumps(json_text),headers=headers).content)
 
if __name__ == '__main__':
    text = sys.argv[1]
    msg(text)
