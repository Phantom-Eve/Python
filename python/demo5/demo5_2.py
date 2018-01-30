#!/usr/bin/evn python
# -*_ coding: utf-8 -*-

classmates = ['Michael', 'Bob', 'Tracy']

# 定义主函数
def main():
	print u"1 输出list长度"
	print u"2 输出list中第三个元素"
	print u"3 输出list中倒数第二个元素"
	print u"4 list新增元素'Adam'"
	print u"5 在第一个元素之后插入新元素'Jack'"
	print u"6 删除list末尾的元素"
	print u"7 删除list指定位置的元素"
	print u"8 替换某个指定元素"
	no = raw_input(unicode('请输入你想执行操作的序号：','utf-8').encode('gbk'))
	operateList(no)
	
# 定义用来操作List的函数
def operateList(no):
	if "0"==no:
		return

	# 设置正确序号的开关
	flag = True	
	# 输出list长度
	if "1"==no:
		print u"list长度为：",len(classmates)

	# 输出list中第三个元素
	elif "2"==no:
		print classmates[2]

	# 输出list中倒数第二个元素
	elif "3"==no:
		print classmates[-2]

	# list新增元素
	elif "4"==no:
		classmates.append('Adam')
		print u"新增元素后list长度为：",len(classmates)
		print u"list的最后一个元素是：",classmates[-1]

	# 在第一个元素之后插入新元素
	elif "5"==no:
		classmates.insert(1, 'Jack')
		print u"插入元素后list长度为：",len(classmates)
		print u"list的第二个元素是：",classmates[1]

	# 删除list末尾的元素
	elif "6"==no:
		classmates.pop()
		print u"删除元素后list长度为：",len(classmates)
		print u"list的最后一个元素是：",classmates[-1]

	# 删除list指定位置的元素
	elif "7"==no:
		classmates.pop(1)
		print u"删除元素后list长度为：",len(classmates)
		print u"list的第二个元素是：",classmates[1]

	# 替换某个指定元素
	elif "8"==no:
		print u"替换前list第一个元素是：",classmates[1]
		classmates[1] = 'Sarah'
		print u"替换后list第一个元素是：",classmates[1]

	else:
		flag = False
		no = raw_input(unicode('您输入的序号不正确，请重新输入：','utf-8').encode('gbk'))
		operateList(no)

	if flag:
		no = raw_input(unicode('请继续输入操作序号,结束请按0：','utf-8').encode('gbk'))
		operateList(no)

# 调用主函数
print u"===================# 调用主函数 begin==================="
main()
print u"===================# 调用主函数 begin==================="