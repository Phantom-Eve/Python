#!/usr/bin/evn python
# -*_ coding: utf-8 -*-

# 使用列表生成式创建list 
print u"===================# 使用循环创建x*x的list ==================="
L = []
for x in range(1,11):
	L.append(x * x)
print u"使用循环创建的list：",L

print u"\n===================# 使用列表生成式创建x*x的list ==================="
L1 = [x * x for x in range(1,11)]
print u"使用列表生成式创建的list：",L1

print u"\n===================# 使用列表生成式创建x*x的list(仅偶数) ==================="
L2 = [x * x for x in range(1,11) if x % 2 == 0]
print u"使用列表生成式创建的list(仅偶数)：",L2

print u"\n===================# 使用列表生成式创建'ABC'和'XYZ'的全排列 ==================="
L3 = [m + n for m in "ABC" for n in "XYZ"]
print u"使用列表生成式创建'ABC'和'XYZ'的全排列：",L3


# 列出当前目录下的所有文件和目录名
print u"\n===================# 列出当前目录下的所有文件和目录名 ==================="
import os
dirName = [d for d in os.listdir(".")]
print dirName

# 生成dict的list
print u"\n===================# 生成dict的list ==================="
dict = {1:'Michael', 2:'Sarah', 3:'Tracy', 4:'Bob', 5:'Jack'}
L4 = [str(k) + "=" + v for k, v in dict.iteritems()]
print u"dict的list：", L4

# 把一个list中所有的字符串变成小写
print u"\n===================# 把一个list中所有的字符串变成小写 ==================="
upper = ['Hello', 'World', 18, 'IBM', 'Apple']
lower = [s.lower() if isinstance(s, str) else s for s in upper]
print u"含大写字母的list：",upper
print u"全小写字母的list：",lower
