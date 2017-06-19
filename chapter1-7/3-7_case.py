#!/usr/bin/python
# coding=utf8

vip = ['Tesla','Kobe','Bill','Jordan']

print "Welcome to join us %s" % vip[0]
print "Welcome to join us %s" % vip[1]
print "Welcome to join us %s" % vip[2]
print "Welcome to join us %s" % vip[3]


x = vip[2]
vip[2] = 'Hill'
print
print "%s 由于需要参加巴菲特的股东大会不能出席本次活动，换成%s出席" % (x,vip[2])
print
for i in range(len(vip)):
	print "Welcome to join us %s" % vip[i]

print "由于我找到更大的会场，新增三位嘉宾"

vip.insert(0,'Butu')
vip.insert(3,"Tubo")
vip.append('wuli')

print
for i in range(len(vip)):
	print "Welcome to join us %s" % vip[i]

print 

print "由于新的场次无缺确认，目前只能邀请2位嘉宾"
for i in range(len(vip)-2):
	print "sorry，%s，您无法参加本次活动，下次再邀请您"%vip.pop()

print
for i in range(len(vip)):
	print "Welcome to join us %s" % vip[i]



for i in range(len(vip)):
	del vip[0] #这里如果为vip[i]会报错，因为第二次i就是1，而只有vip[0]

print "vip名单：%s" % vip