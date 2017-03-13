# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 12:47:55 2017

@author: Differlong
"""

import requests
import pickle
from bs4 import BeautifulSoup

#urlList = ["https://www.zhihu.com/question/{}".format(str(i)) for i in range(20000000,41000000)]

def urlPost():
    for i in range(20000000,41000000):
        yield "https://www.zhihu.com/question/{}".format(str(i))
        
    print("Url List is None, End!")
    return None

s = requests.session()

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
           "Upgrade-Insecure-Requests":1
           }

for i in headers:
    s.headers[i] = headers[i]

url = "https://www.zhihu.com/question/20000003"

resp = s.get(url).text
print(resp)


