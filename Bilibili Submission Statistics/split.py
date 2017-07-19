# -*-coding: utf-8 -*-
import re

if __name__=='__main__':
    f=open("data.txt",'r')
    out=open("out.txt",'w')
    out.writelines("av号\t播放量\t\t名称\n")     
    
    cout=0
    line=f.readline()
    while(line!=""):        
        cout=cout+1
        pattern="(\d*)\[<title>(.*)_bilibili_哔哩哔哩</title>\]\s*\['(\d*)'\]"
        #pattern_err=  "(\d*)\[<title>(.*)_bilibili_哔哩哔哩</title>\]\s*\['(\d*)'\]"      

        info=re.findall(pattern,line) 
        if info:    
            res=str(info[0][0])+"\t\t"+str(info[0][2])+"\t\t"+str(info[0][1])+"\n"
        else:
            res="error\n"   
            
        print cout    
        out.writelines(res)                
        line=f.readline()        
    out.close()
    f.close()
