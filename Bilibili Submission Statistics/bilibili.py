# -*- coding: utf-8 -*-
"""
Created on Mon May 08 12:35:38 2017

@author: tyw
"""

import urllib

import gzip
import StringIO
import re
import threading,time,thread

from bs4 import BeautifulSoup
       
def getDianji(index):       
    url="%s%d"%("http://api.bilibili.com/archive_stat/stat?aid=",index)
    f=urllib.urlopen(url)
    content=f.read()
    f.close()
    pattern="\"view\":([0-9]*)"
    number=re.findall(pattern,content)   
    try:
        number=int(number[0])
    except:
        number=0
        
    return number

def getTitle(index):
    url="%s%d"%("http://www.bilibili.com/video/av",index)
    f=urllib.urlopen(url)
    html=f.read()
    f.close()
    data = StringIO.StringIO(html)
    try:
        gzipper = gzip.GzipFile(fileobj=data)    
        content = gzipper.read()
        # 使用BeautifulSoup匹配
        soup = BeautifulSoup(content)
        # 相较通过正则表达式去匹配,BeautifulSoup提供了一个更简单灵活的方式
        #avTitle = soup.findAll("title")    
        #avTitle=soup.html.title.string.encode('utf-8')
        avTitle=soup.html.title.get_text().encode('utf-8')
        #avTitle=soup.html.title.NavigatableString.encode('utf-8')  #这个不行 有待研究
    except:
        avTitle=""
    
    return avTitle
    
    
def doWork(index,output):            
    title=getTitle(index)    
    playNum=getDianji(index)
    line=str(index)+"\t"+str(playNum)+"\t"+title   
    output.writelines(line+"\n")
    if(index%10==0):
        output.flush()
        print line
    

def main():
    fileobj=open("TEMP.txt",'a+')
    for ID in range(331311,400000,2):
        #doWork(ID,fileobj)
        
        t1=threading.Thread(target=doWork(ID,fileobj))
        t2=threading.Thread(target=doWork(ID+1,fileobj))
        #t3=threading.Thread(target=doWork(ID+2,fileobj))  
        #t4=threading.Thread(target=doWork(ID+3,fileobj))                            
        t1.start()  
        t2.start() 
        #t3.start()  
        #t4.start() 
        t1.join()
        t2.join()
        #t3.join()  
        #t4.join() 
             
    fileobj.close()
  
if __name__ == '__main__':
    startime=time.time()
    main()
    endtime=time.time()
    print "用时：",endtime-startime


