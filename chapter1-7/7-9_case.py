#!/usr/bin/python
# coding=utf8

# 7-9 五香烟熏牛肉（pastrami）卖完了：使用为完成练习7-8 而创建的列表
# sandwich_orders，并确保'pastrami'在其中至少出现了三次。在程序开头附近添加这样
# 的代码：打印一条消息，指出熟食店的五香烟熏牛肉卖完了；再使用一个while 循环将
# 列表sandwich_orders 中的'pastrami'都删除。确认最终的列表finished_sandwiches 中
# 不包含'pastrami'。

sandwich_orders = ['tuna','pastrami','Panini','pastrami','Mozzarella','pastrami']

print 'Sorry ,we are out of  pastrami'

while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')

print 'All we have are: \n'
for s in sandwich_orders:
	print s,