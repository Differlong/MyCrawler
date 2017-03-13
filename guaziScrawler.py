# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 16:44:50 2016

@author: Differlong
"""

import requests
from bs4 import BeautifulSoup
import profile
url = "http://www.guazi.com/bj/3000000001x.htm"
import time

def myPrint():
    time.sleep(3)
    print("Hello World")


def geturl(url,file):
    try:
        resp = requests.get(url).text
    except Exception as e:
        print("Connection Error: ",e,"\n----",url)
        return None

    soup = BeautifulSoup(resp,"lxml")
    
    header = soup.find("h1",{"class":"dt-titletype"}).text
    print(header,file=file)
    imgs = soup.findAll("li",{"data-role":"thumb"})
    #7的意思是为了只提取外观的照片
    for i in range(min(7,len(imgs))):
        src = imgs[i].img.get("src").split("@")[0]
        print(src,file=file)

#现在图片地址都ok了，需要把最后@后面的参数去掉

"""
urls = "http://www.guazi.com/bj/{}x.htm".format(str(i) for i in range(3000000001,3000559801))
with open("瓜子二手车图片数据.txt","w") as file:
    for i in range(3000000001,3000001801):
        url = "http://www.guazi.com/bj/" + str(i) + "x.htm"
        geturl(url,file)

with open("test.txt","w") as file:
    profile.run("geturl(url,file)")
"""