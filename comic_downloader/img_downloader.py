# -*- coding: utf-8 -*-
"""
Created on 2018/9/8

@author: tyw66
"""

import urllib
import requests
from bs4 import BeautifulSoup

import re

import os 
import time

from traits.api import HasTraits
from traits.api import Int,Str,Float
from traitsui.api import View,Item,OKCancelButtons

##全局变量
##模拟构造请求头，会话
session = requests.Session()
headers = {
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
}
	
	
##获取网页标题
def getTitle(url):
	req=session.get(url,headers=headers)
	html=req.text
	
	bsObj = BeautifulSoup(html, "html.parser")
	title = bsObj.find("title").text

	return title
    
##标题处理,新建文件夹
def title2folder(title):
	title = title.strip()
	title = re.sub('[\r\n\|\.\<\>\*]','',title)

	folder = "%s%s"%("./",title)
	#print folder
	return folder
	
##下载url链接中的所有图片到folder目录下
def downloadImages(url,folder,page_count):
	print "downloadImages:",url
	
	req=session.get(url,headers=headers)
	html=req.text
	
	##没有模拟头 会被ban
	#f=urllib.urlopen(url)
	#html=f.read()
	#print html
	#f.close()		
	
	bsObj = BeautifulSoup(html, "html.parser")
	pattern = re.compile(".*\.jpg")
	img_node_list=bsObj.findAll("img",{"src":pattern})
	
	count=0
	for node in img_node_list:
		img_url = node["src"]
		if(img_url[0:4]!="http"):
			img_url="%s%s"%("https:",img_url)	#（针对部分情况）添加"http:"头
		print img_url
		
		count+=1
		img_name = "%s%s%d%s%d%s"%(folder,"/page",page_count,"_",count,".jpg")
		#print img_name
		
		##没有模拟头 会被ban
		#urllib.urlretrieve(img_url,img_name)
		
		##解析图片，写入到本地
		req=session.get(img_url,headers=headers)
		f = open(img_name, "wb")
		f.write(req.content)
		f.close()
	
	
def main(mainUrl,subUrl,subFix,N):


	title=getTitle(mainUrl)
	folder = title2folder(title)
	if not os.path.exists(folder):
		os.mkdir(folder)
	
	
	if N>0:
		for page_count in range(1,N+1):
			url="%s%s%d%s"%(mainUrl,subUrl,page_count,subFix)		
			downloadImages(url,folder,page_count)
	else:	
		downloadImages(mainUrl,folder,1)
	
		
			
#UI界面
class UiClass(HasTraits):
	pageNum=Int(0)
	mainUrl=Str("https://one-piece.cn/post/10916/")
	subUrl=Str("")
	subFix=Str("")
	
	View=View(
		Item('pageNum',label=u"页数，无分页模式输入0"),
		Item('mainUrl',label=u"主网址"),
		Item('subUrl',label=u"补充，如/index1，无分页模式留空"),
		Item('subFix',label=u"网页后缀，如.html，无分页模式留空"),
		title=u"输入",
		width=1000,
		height=100,
		resizable=True,  
		buttons=OKCancelButtons
	)		
	


if __name__ == '__main__':
	startime=time.time()
	ui=UiClass()
	ui.configure_traits()	
	main(ui.mainUrl, ui.subUrl, ui.subFix, ui.pageNum)
	endtime=time.time()
	print u"下载完毕，用时：",endtime-startime



'''
神秘网站
	"https://guguxx.biz/artkt/DTgongfangDAIGOchongjinsuonianfu40P/"
	

'''
	