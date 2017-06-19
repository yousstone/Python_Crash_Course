#!/usr/bin/python
# coding=utf8

# 7-8 熟食店：创建一个名为sandwich_orders 的列表，在其中包含各种三明治的名
# 字；再创建一个名为finished_sandwiches 的空列表。遍历列表sandwich_orders，对于
# 其中的每种三明治，都打印一条消息，如I made your tuna sandwich，并将其移到列表
# finished_sandwiches。所有三明治都制作好后，打印一条消息，将这些三明治列出来。

sandwich_orders = ['tuna','Panini','Mozzarella']
finished_sandwiches = []

while sandwich_orders:
	s = sandwich_orders.pop()
	print 'I made your %s sandwich' % s
	finished_sandwiches.append(s)

print 'All finished_sandwiches are : '

for ss in finished_sandwiches:
	print ss,