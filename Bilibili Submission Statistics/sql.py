#!/usr/bin/python
import sqlite3
import sys
reload(sys)
sys.setdefaultencoding('utf8')


conn=sqlite3.connect('bilibili.db')

f=open("test.txt",'r')
#line=f.readline()
#while(line):
#    print line
#    line=f.readline()    

for line in f:
    item=line.split("\t")
#    cmd="INSERT INTO PlayList VALUES(%s,%s,%s,%s,%s)"%(str(item[0]),str(item[1]),str(item[2]),str(item[3]),str(item[4])
#    conn.execute(cmd)#    
    conn.execute("INSERT INTO PlayList VALUES(%s,%s,%s,%s,%s)"%(str(item[0]),str(item[1]),str(item[2]),str(item[3]),str(item[4])))
    print line

print "success!"