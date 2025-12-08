
import hashlib
import json
import pprint
import random
import re
from itertools import groupby
from operator import itemgetter
import time
import pandas as pd
import requests
import pdb


def get_completion(message, address):


    url = 'https://qianfan.baidubce.com/v2/chat/completions'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer bce-v3/ALTAK-9mrsJ85ZgN7GOCiywfcA1/b67875ad80c340ff6f819865b79fcef6c015d44b'
    }
    data = {
        "model": address,
        "messages": 
        # [
        #     {
        #         "role": "user",
        #         "content": message
        #     }
        # ]
        message
    }
    # pdb.set_trace()
    response = None
    
    
    while not response:
        
        try:
            st_time=time.time()
            response = requests.post(url, headers=headers, json=data)
            # print(f"{time.time()-st_time:.6}")
            # print(response.text)
            # res_text = response.text
            # pdb.set_trace()
            return json.loads(response.text)["choices"][0]['message']['content']
            # return json.loads(response)["choices"][0]['message']['content']
        except :
            time.sleep(1)
            # print("get_completion"+address+'请求失败'+str(fail_num)+'次')
            continue





if __name__=="__main__":
    print(get_completion("你能给我讲个笑话吗？", "w8smrcmj_l0408comfort_spd"))
