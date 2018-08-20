#!/usr/bin/evn python
# -*_ coding: utf-8 -*-

# 高阶函数-变量可以指向函数
print u"\n===================# 使用abs()求绝对值 ==================="
print u"abs(-10) =", abs(-10)

print u"\n===================# 把函数赋值给变量f后，使用变量f求绝对值 ==================="
f = abs
print u"f(-10) =", f(-10)

# 高阶函数-传入函数
print u"\n===================# 利用传入函数进行绝对值求和 ==================="
def add(x, y, f):
	return f(x) + f(y)
print u"add(-5, 6, abs) =", add(-5, 6, abs)