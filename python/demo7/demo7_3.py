#!/usr/bin/evn python
# -*_ coding: utf-8 -*-

# 匿名函数lambda
print u"\n===================# 匿名函数lambda ==================="
def f(x):
	return x * x

print u"\n使用显示函数计算f(x)=x2", map(f, [1, 4, 9, 16, 25, 36, 49, 64, 81])
print u"\n使用匿名函数计算f(x)=x2", map(lambda x : x * x, [1, 4, 9, 16, 25, 36, 49, 64, 81])

print u"\n===================# 把匿名函数作为返回函数 ==================="
f = lambda x : x * x
print u"输出匿名返回函数：", f(5)
