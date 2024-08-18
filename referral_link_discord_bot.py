# -*- coding: utf-8 -*-

import requests
import json
import random
import time

def get_context():
    variables = [
        "testing\n",
    ]
    return ''.join(variables)

def chat(chanel_list,authorization_list):
    for authorization in authorization_list:
        header = {
            "Authorization": authorization,
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
        }
        for chanel_id in chanel_list:
            msg = {
                "content": get_context(),
                "nonce": "82329451214{}33232234".format(random.randrange(0, 1000)),
                "tts": False,
            }
            url = "https://discord.com/api/v9/channels/{}/messages".format(chanel_id)
            try:
                res = requests.post(url=url, headers=header, data=json.dumps(msg))


            except:
                pass
            continue

if __name__ == "__main__":
    chanel_list = ["1"
    ,"1274583269232345154"]
    authorization_list = [""]
    chat(chanel_list,authorization_list)

