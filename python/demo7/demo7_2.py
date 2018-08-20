#!/usr/bin/evn python
# -*_ coding: utf-8 -*-

# 返回函数
print u"\n===================# 返回函数 ==================="
def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax = ax + n
		return ax
	return sum
f = lazy_sum(1, 3, 5, 7, 9)

print u"调用返回函数：", f()