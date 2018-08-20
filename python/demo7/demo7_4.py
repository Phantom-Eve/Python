#!/usr/bin/evn python
# -*_ coding: utf-8 -*-
import functools

# 装饰器Decorator
print u"\n===================# 在代码运行期间动态增加功能的方式，称之为“装饰器” ==================="
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator

def nowBef():
	print "2018-08-20"

# 使用装饰器装饰函数
@log("excute")
def now():
	print "2018-08-20"

print u"调用装饰器处理前的now函数："
nowBef()
print u"调用装饰器处理后的now函数："
now()

print u"\n===================# 在函数调用的前后打印出'begin call'和'end call'的日志 ==================="
def logs(begin, end):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print '%s %s()' % (begin, func.__name__)
			result = func(*args, **kw)
			print '%s %s()' % (end, func.__name__)
			return result
		return wrapper
	return decorator

@logs("begin call", "end call")
def test():
	print u"测试前后日志"

print u"在函数调用的前后打印日志："
test()