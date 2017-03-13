# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 21:18:12 2016

@author: 独处
"""

import requests
from bs4 import BeautifulSoup
import threading
import os

basePath = "F:/美图录"#存储的位置
threadLimit = 10#下载线程数目




os.chdir(basePath)

urlPool = ["http://www.meitulu.com/item/{}.html".format(str(i))for i in range(8601,8699)]
numMutex = threading.Lock()
#以g开头，意味着这是一个全局变量
g_threadNum = 0

def downloadImg(url):
    dirname = url.split("/")[-1].split(".")[0]
    if not os.path.isdir(dirname):
        os.mkdir(dirname)
    ordinal = 1
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36"}
    linkPool = []
    while True:
        try:
            resp = requests.get(url,headers=headers).text
            soup = BeautifulSoup(resp,"lxml")
            links = soup.select("body > div.content > center > img")
            for urlLink in links:
                link = urlLink.get("src")
                linkPool.append(link)
            nextPageUrl = soup.findAll("a",{"class":"a1"})[1].get("href")
            if nextPageUrl == url :
                
                break
            else:
                url = nextPageUrl
        except Exception:
            #这里没有用锁，好吧，也就这样了，应该不会出现什么问题吧，最多是不好看而已
            print("Connection Error, or BeautifulSoup going Wrong, forget it:",url)
            break
            
    for link in linkPool:
        try:
            content = requests.get(link,headers = headers)
            title = str(ordinal) + ".jpg"
            #文件就保存在工作目录了
            file = open(dirname +"/" + title,"wb")
            file.write(content._content)
            file.close()
            ordinal += 1
        except Exception :
            print("Couldn't Parse!",link)
            break






   

class MyThread(threading.Thread):
    def __init__(self,url):
        self.url = url
        threading.Thread.__init__(self)
    
    def run(self):
        downloadImg(self.url)
        numMutex.acquire()
        global g_threadNum
        g_threadNum -= 1
        numMutex.release()


while urlPool != []:
    #如果线程比较少，就
    if g_threadNum < threadLimit:
        newUrl = urlPool.pop()
        g_threadNum += 1
        newThread = MyThread(newUrl)
        newThread.start()
    

    
    





