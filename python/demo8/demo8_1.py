#!/usr/bin/evn python
# -*_ coding: utf-8 -*-

'a test module'

__author__ = 'Phantom'

import sys

# 使用模块
print u"\n===================# 使用模块 ==================="

def test():
	args = sys.argv
	if len(args) == 1:
		print 'Hello, world'
	elif len(args) ==2:
		print 'Hello, %s' % args[1]
	else:
		print 'Too many arguments!'

if __name__ == '__main__':
	test()

print u"\n===================# 变量作用域 ==================="

def _private_1(name):
	return 'Hello, %s' % name

def _private_2(name):
	return 'Hi, %s' % name

def greeting(name):
	if len(name) > 3:
		return _private_1(name)
	else:
		return _private_2(name)

if __name__ == '__main__':
	print greeting('slx')