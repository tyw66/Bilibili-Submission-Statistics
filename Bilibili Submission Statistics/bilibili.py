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

import time

from bs4 import BeautifulSoup
       
#获取播放量数据
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

##获取网页标题
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
	playNum=getDianji(index)
	##只抓取播放量大于100万的视频信息
	if(playNum>1000000):
		title=getTitle(index)    
		line=str(index)+"\t"+str(playNum)+"\t"+title   
		output.writelines(line+"\n")
	if(index%100==0):
		print index
		output.flush()
		#print line
    

def main():
	fileobj=open("TEMP.txt",'a+')
	N=4
	for ID in range(22906/N,20000000/N,1):
		#print ID*N
		#doWork(ID,fileobj)		
		
		t1=threading.Thread(target=doWork(N*ID+1,fileobj))
		t2=threading.Thread(target=doWork(N*ID+2,fileobj))
		t3=threading.Thread(target=doWork(N*ID+3,fileobj))  
		t4=threading.Thread(target=doWork(N*ID+4,fileobj))  
		#t5=threading.Thread(target=doWork(N*ID+5,fileobj))  
		#t6=threading.Thread(target=doWork(N*ID+6,fileobj))
		#t7=threading.Thread(target=doWork(N*ID+7,fileobj))
		#t8=threading.Thread(target=doWork(N*ID+8,fileobj))  
		#t9=threading.Thread(target=doWork(N*ID+9,fileobj))  
		#t10=threading.Thread(target=doWork(N*ID+10,fileobj))  		
		t1.start()  
		t2.start() 
		t3.start()  
		t4.start()
		#t5.start()
		#t6.start()  
		#t7.start() 
		#t8.start()  
		#t9.start()
		#t10.start()
		t1.join()
		t2.join()
		t3.join()  
		t4.join() 
		#t5.join()
		#t6.join()
		#t7.join()
		#t8.join()  
		#t9.join() 
		#t10.join()
	fileobj.close()

if __name__ == '__main__':
    startime=time.time()
    main()
    endtime=time.time()
    print "用时：",endtime-startime


