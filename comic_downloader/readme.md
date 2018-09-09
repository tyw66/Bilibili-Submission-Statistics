# 漫画爬取器
## 漫画网站URL规则:
- URL形如："{漫画主地址名}/{附加名}{序号}{后缀}"

	福利eg. https://guguxx.biz/artkt/DTgongfangDAIGOchongjinsuonianfu40P/index_1.html
	
	序号从1开始递增，和页数相同
	
- 输入

	网址：https://guguxx.biz/artkt/DTgongfangDAIGOchongjinsuonianfu40P/
	
	总页数：4
	
	附加：index_
	
	后缀：.html
	
- 输出
	
	程序在当前目录下生成文件夹存放图片，文件夹命名为网页title
	
	
## 特点	
- 使用用traitsui做界面


## 例子：

### 海贼王漫画
用户输入

	- 网址：https://one-piece.cn/post/10916/
	
	- 总页数：0
	
	- 附加：（留空）
	
	- 后缀：（留空）
	
### 福利漫画
用户输入

	- 网址：https://guguxx.biz/artkt/DTgongfangDAIGOchongjinsuonianfu40P/
	
	- 总页数：4
	
	- 附加：/index
	
	- 后缀：.html
	
	
## 问题记录
- configure_traits()这个函数新版本好像有问题？用python_sci提供的那个版本库可以。
- 文件夹名字编码乱码的情况
