#!/usr/bin/evn python
# -*_ coding: utf-8 -*-

dict = {1:'Michael', 2:'Sarah', 3:'Tracy', 4:'Bob', 5:'Jack'}

# 使用for循环进行迭代
print u"===================# 使用for循环进行迭代 ==================="
# 迭代dict的key
print u"\n迭代dict的key："
for key in dict:
	print u"key:",key

# 迭代dict的value
print u"\n迭代dict的value："
for value in dict.itervalues():
	print u"value:",value

# 同时迭代key和value
print u"\n同时迭代key和value："
for k, v in dict.iteritems():
	print u"key-value",k,"-",v

# 判断一个对象是否可以迭代
print u"\n===================# 判断一个对象是否可以迭代 ==================="
from collections import Iterable
# str是否可迭代
print u"str是否可迭代：",isinstance('abc', Iterable) 
# list是否可迭代
print u"list是否可迭代：",isinstance('[1,2,3]', Iterable) 
# str是否可迭代
print u"整数是否可迭代：",isinstance(123, Iterable) 

print u"\n===================# 使用enumerate进行下标循环 ==================="
for i, value in enumerate(['A', 'B', 'C']):
	print u"index-value",i,value