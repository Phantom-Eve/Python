#!/usr/bin/evn python
# -*_ coding: utf-8 -*-

# 绝对值函数abs(num)
print u"===================# 绝对值函数abs(num)==================="
num = int(raw_input("请输入需要求绝对值的数字：".decode('utf-8').encode('gbk')))
absNum = abs(num)
print num,u"的绝对值为：",absNum
print ""

# 比较函数cmp(x, y)
print u"===================# 比较函数cmp(x, y)==================="
x = int(raw_input("请输入数字x：".decode('utf-8').encode('gbk')))
y = int(raw_input("请输入数字y：".decode('utf-8').encode('gbk')))
if cmp(x, y)>0:
	print u"x大于y"
elif cmp(x, y)==0:
	print u"x等于y"
else:
	print u"x小于y"
print ""