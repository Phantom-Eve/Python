#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 条件判断
print u"===================# 条件判断==================="
age = raw_input("请输入您的年龄:".decode('utf-8').encode('gbk'))
# 类型强转
age = int(age)

if age >= 18:
	print u"成年"
elif age >= 0 & age < 18:
	print u"未成年"
else:
	print u"您输入的年龄不合法" 
print ""

# for...in循环
print u"===================# for...in循环==================="
names = ['小陈', '小皮', '大陈']
for name in names:
	print name.decode("utf-8").encode("gbk")

sum = 0
for x in range(101):
	sum = sum + x
print "0+1+2+...+99+100 =",sum
print ""

# while循环
print u"===================# while循环==================="
s = 0
n = 99
while n > 0:
	s = s + n
	n -= 2
print "100以内所有奇数之和为：",s
print ""