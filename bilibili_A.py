# -*- coding: utf-8 -*-
"""
Created on Mon May 08 12:35:38 2017

@author: tyw
"""

import urllib
import gzip
import StringIO
import re

from bs4 import BeautifulSoup



       
def getDianji(index):       
    url="%s%d"%("http://api.bilibili.com/archive_stat/stat?aid=",index)
    f=urllib.urlopen(url)
    content=f.read()
    f.close()
    pattern="\"view\":([0-9]*)"
    number=re.findall(pattern,content)    
    return number

def getName(index):
    url="%s%d"%("http://www.bilibili.com/video/av",index)
    f=urllib.urlopen(url)
    html=f.read()
    f.close()
    data = StringIO.StringIO(html)

    gzipper = gzip.GzipFile(fileobj=data)    
    content = gzipper.read()


    # 使用BeautifulSoup匹配
    soup = BeautifulSoup(content)
    # 相较通过正则表达式去匹配,BeautifulSoup提供了一个更简单灵活的方式
    avTitle = soup.findAll("title")
    res=str(avTitle)
    
    return res
    
    
def doSome(index):            
    #title=getName(index)
    playNum=getDianji(index)
    line=str(index)+"\t"+str(playNum)
    return line
    

def main():
    fileobj=open("TEMP.txt",'a+')
    for i in range(150001,200000):
        line=doSome(i)
        
        print line
        fileobj.writelines(line+"\n")
        if(i%100==0):
            fileobj.flush()        
    fileobj.close()
  
if __name__ == '__main__':
    main()


