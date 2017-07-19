# --*--coding:utf-8 --*--
from urllib import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://en.wikipedia.org/wiki/kevin_Bacon")
bsObj = BeautifulSoup(html)

print "原始的 获取了所有页内链接"
for link in bsObj.findAll():
        if 'href' in link.attrs:
            print(link.attrs['href'])

print '改进的 利用规则 仅获取指向其他词条的链接'
for link in bsObj.find("div",{"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$")):
    if 'href' in link.attrs:
        print(link.attrs['href'])



# html=urlopen("http://www.bilibili.com/av123456")
# bsObj=BeautifulSoup(html)
# bsObj.find_all('img','href')