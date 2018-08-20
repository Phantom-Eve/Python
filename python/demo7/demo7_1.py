#!/usr/bin/evn python
# -*_ coding: utf-8 -*-

# map/reduce接收两个参数：1.函数，2.序列
L = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print u"\n===================# map将传入的函数依次作用到序列的每个元素 ==================="
print u"使用map把数字list转化为字符串：", map(str, L)

print u"\n===================# reduce把一个函数作用在一个序列上 ==================="
# 集合求和
def add(x, y):
	return x + y
print u"使用reduce对list求和：", reduce(add, L)

#　规范名字（首字母大写，其它字母小写）
print u"\n利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字"
names = ['adam', 'LISA', 'barT']
def format(s):
	return s.title()

print u"输入：", names
print u"输出：", map(format, names)

print u"\n利用reduce()函数，接受一个list并求积"

# 集合求积
prodList = [1, 2, 3, 4, 5]
def prod(x, y):
	return x * y

print u"集合：", prodList
print u"list求积：", reduce(prod, prodList)



print u"\n===================# filter把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素 ==================="
def is_odd(n):
	return n%2 == 1

print u"删掉list中的偶数，只保留奇数：", filter(is_odd, L)

# 删除1~100的素数
priList = range(1, 101)
def is_prime(n):
	if n == 1:
		return True
	for i in range(2, n):
		if n % i == 0:
			return False
	return True

print u"删除1~100的素数：", filter(is_prime, priList)



print u"\n===================# sorted()函数可以对list进行排序 ==================="
def desc_sort(x, y):
	if x > y:
		return -1
	if x < y:
		return 1

print u"实现倒序排序：", sorted([36, 5, 12, 9, 21], desc_sort)

# 忽略大小写对字母进行排序
def cmp_ignore_case(x, y):
	x = x.upper()
	y = y.upper()
	if (x > y):
		return 1
	if (x < y):
		return -1
print u"忽略大小写来比较两个字符串：", sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)
