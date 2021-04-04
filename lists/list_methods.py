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

# Append() method is used to add the values at the end of the list
mylist = ['ram', 'tcp_ip protocols', 'dhcp', 'dns']
mylist.append("Router")
print(mylist)

# pop() method is used to remove specific index value in a list 
# if you don't provide the index value in the pop method then it will remove the last item
mylist = ['ram', 'tcp_ip protocols', 'dhcp', 'dns']
mylist.pop(-1)
print(mylist)

# Another example
mylist = ['ram', 'tcp_ip protocols', 'dhcp', 'dns']
mylist.pop() # if you don't specify the index value in the pop method then it will remove the last item
print(mylist)

#del is a keyword
mylist = ['ram', 'tcp-ip protocols', 'dhcp', 'dns']
del mylist # this will delete entire list 

# you can also use del keyword to remove specific indexed value in a list 
mylist = ['ram', 'tcp-ip protocols', 'dhcp', 'dns']
del mylist[0]
print(mylist)

# copy command is used to copy a certain list to another list 
mylist = ['ram', 'tcp-ip protocols', 'dhcp', 'dns']
mylist1 = mylist.copy()

# remove() method is used to remove a certain value in a list
mylist = ['ram', 'tcp-ip protocols', 'dhcp', 'dns']
mylist.remove('dhcp')
print(mylist)

# clear method clears the entire list.
mylist = ['ram', 'tcp-ip protocols', 'dhcp', 'dns']
mylist.clear()
print(mylist)

#reverse method is used to reverse the list
mylist = ['ram', 'tcp-ip protocols', 'dhcp', 'dns']
mylist.reverse()
print(mylist)

#count() method return number how many times that the selected value apperas in the list.
mylist = ['ram', 'tcp-ip protocols', 'dhcp', 'ram']
count = mylist.count('ram')
print(count)

#index() method return the index of the specified value 
mylist = ['ram', 'tcp-ip protocols', 'dhcp', 'ram']
position = mylist.index('dhcp')
print(position)

