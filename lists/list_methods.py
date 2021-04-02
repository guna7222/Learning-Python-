'''
insert()
extend()
append()
pop()
del is a key word
copy()
remove(value)
clear()
reverse()
count()
index()
'''

# insert() method is used to insert a value in a list at a specified index.
mylist = ['ram', 'tcp_ip protocols', 'dhcp', 'dns']
mylist.insert(4, 'ADS')
print(mylist)

# example
mylist = ['ram', 'tcp-ip protocols', 'dhcp', 'dns']
mylist.insert(9, 'ADS')
print(mylist)

#extend() method adds a another list with a current list 
mylist = ['ram', 'tcp-ip protocols', 'dhcp', 'dns']
mylist1 = ['outlook', 'network_printers', 'local_printers']
mylist.extend(mylist1)
print(mylist)

# experiment 
mylist = ['ram', 'tcp-ip protocols', 'dhcp', 'dns']
mylist1 = ['outlook', 'network_printers', 'local_printers']
output = mylist.extend(mylist)
print(output)
# Ans:- None