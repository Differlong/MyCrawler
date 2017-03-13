# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 18:44:44 2016

@author: diffe
"""

import requests
from bs4 import BeautifulSoup
import re

session = requests.Session()
session.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
session.get("https://www.c5game.com")



def getApi(url,session=session):
    #检验正确了
    #数据是resp，该开始的html形式，需要进行处理，直接输出想要的结果好了，没有必要造这么多的轮子，先把事情完成了再说
    try:
        resp = session.get(url).json()
    except Exception as e:
        print("Position[0],Error is:",e)
        return None
    else:
        if resp["status"] != 200:
            return None
        price = resp["body"]["items"][0]["price"]
        return price


        

def getHtml(url,session=session):
    totalNum = 0
    sellNum = 0
    buyNum = 0
    name = "Default"
    try:
        resp = session.get(url).text
    except Exception as e:
        print("[Error 1]",url,e)
    else:
        soup = BeautifulSoup(resp,"lxml")
        p1 = soup.findAll("div",{"class":"sale-item-num"})
        pattern = re.compile("\d+")
        totalNum = int(re.findall(pattern,p1[0].text)[0])
        p2 = soup.findAll("li",{"role":"presentation"})
        sellNum = int(re.findall(pattern,p2[0].text)[0])
        buyNum = int(re.findall(pattern,p2[1].text)[0])
        name = soup.find("div",{"class":"name"}).text
        api = soup.find("tbody",{"data-tpl":"sale-tpl"}).get("data-url")
        api = "https://www.c5game.com" + api
    return (name,totalNum,sellNum,buyNum,api)








class Accessory(object):
    def __init__(self,url):
        #单纯这么点数据是估计不出走势的。还是使用小时图好了，到时候绘在图上是不看时间的，看价格走势就好了，这样更加精确，小时，然后按小时存储，相同则求平均
        #需要知道的是名称，url，获取卖的api信息的地址，已经卖出去的数量，待卖的数量，想买的人的数量，根据这些历史数据，然后推断出是否值得入手。
        self.url = url
        self.name = ""
        self.api = ""
        self.totalNum = ""
        self.sellNum = None
        self.buyNum = None
        self.Price = ""
        self.history = {}#存储历史价格的时间线。可以按天存储，也可以按小时来存储，需要对应日期，根据交易价格来查看是否合理,字典存储时间序列吗？
        self.initialize()
    
    def inittialize(self,s=None):
        if s == None:
            self.name,self.totalNum,self.sellNum,self.buyNum,self.api = getHtml(self.url)
    
    def pridict(self):
        pass
    
    def shouldBuy(self):
        pass
    def isUp(self):
        #1,0,-1
        pass
    def isMake(self):
        pass
    def follow(self):
        #跟踪一段时间，确定是否如此的走势
        pass
    
        






class Scrawler(object):
    def __init__(self):
        self.session = requests.Session()
        self.session.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
        self.session.get("https://www.c5game.com")
        #主要做的事page的scrawler
    def getApi(self,Id):
        #返回获得所有数据的字典
        url = "https://www.c5game.com/api/product/sale.html?id={}&page=1".format(Id)
        try:
            resp = self.session.get(url).json()
        except Exception as e:
            print("Position[0],Error is:",e)
            return None
        else:
            return resp
    
