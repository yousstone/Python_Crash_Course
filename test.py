
# string2 = 'my-name-is-michael'
# string3 = string2.split('-')
# print string3
# strint4 = '_'.join(string3)
# print strint4
# string5 = string2.replace('-','_')
# print string5

# string6 = string2.split('-',1)
# print string6
# string7 = '_'.join(string6)
# print string7

# string8 = string2.replace('-','_',1)
# print string8

num_list = []

for i in range(1,10):
	num_list.append(str(i))

print num_list

print ''.join(num_list)
print '_'.join(num_list)
print '-'.join(num_list)

print num_list[::-1]