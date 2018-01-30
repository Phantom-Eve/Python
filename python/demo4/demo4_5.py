#!/usr/bin/evn python
# -*_ coding: utf-8 -*-

# dict
print "===================# dict==================="
d = {'czh':'处女座', 'gry':'金牛座', 'czr':'射手座'}
name = raw_input("请输入姓名：".decode('utf-8').encode('gbk'))
print name,"的星座是：".decode('utf-8').encode('gbk'),d[name].decode('utf-8').encode('gbk')

delName = raw_input("请输入要删除的姓名：".decode('utf-8').encode('gbk'))
print "删除的是：".decode('utf-8').encode('gbk'),delName,d[delName].decode('utf-8').encode('gbk')
d.pop(delName)
print ""

# set
print "===================# set==================="
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
s3 = s1 & s2
s4 = s1 | s2
print "s1:",s1,u"与s2:",s2,u"的交集为:",s3
print "s1:",s1,u"与s2:",s2,u"的并集为:",s4