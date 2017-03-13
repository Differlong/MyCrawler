# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 16:44:50 2016

@author: Differlong
"""

import requests
from bs4 import BeautifulSoup
url = "http://www.guazi.com/bj/3000000001x.htm"



def geturl(url,file):
    """
    抓取瓜子二手车汽车网页的汽车前七张照片，然后保存到file里面。
    """
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
if __name__ == "__main__":
    #urls = "http://www.guazi.com/bj/{}x.htm".format(str(i) for i in range(3000000001,3000559801))
    with open("瓜子二手车图片数据.txt","w") as file:
        for i in range(3000000001,3000001801):
            url = "http://www.guazi.com/bj/" + str(i) + "x.htm"
            geturl(url,file)
