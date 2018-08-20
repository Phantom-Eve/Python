#!/usr/bin/evn python
# -*_ coding: utf-8 -*-
import functools

# 使用functools.partial创建偏函数
print u"\n===================# 使用functools.partial创建偏函数 ==================="
int2 = functools.partial(int, base=2)

print u"把二进制字符串转换为整数：", int2("1000000")