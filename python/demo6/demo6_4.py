#!/usr/bin/evn python
# -*_ coding: utf-8 -*-

# 使用生成器创建list 
print u"\n===================# 使用生成器创建list ==================="
g = (x * x for x in range(1,11))
for n in g:
	print n


# 生成斐波那契数列 
print u"\n===================# 生成斐波那契数列 ==================="
# 定义主函数
def main():
	no = raw_input(unicode('输入需要生成的斐波那契数列个数：','utf-8').encode('gbk'))
	fibList = [n for n in fib(int(no))]
	print fibList
		

# 定义斐波那契数列生成函数
def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield b
		a, b = b, a + b
		n = n + 1

# 调用主函数
main()