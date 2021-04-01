# Removing list items 
# remove() method is used to remove specific elements 
rm = ['python', 'html', 'css', 'bootstrap']
rm.remove('css')
print(rm)

# to remove specific index we will use pop() method 
rm = ['python', 'html', 'css', 'bootstrap']
rm.pop(1)
print(rm)
'''
if you didn't specify the index then pop() will remove last item
'''
rm = ['python', 'html', 'css', 'bootstrap']
rm.pop()
print(rm)

# to delete entire list we can use del keyword
rm = ['python', 'html', 'css', 'bootstrap']
del rm

# you can also delete specific index using del keyword 
rm = ['python', 'html', 'css', 'bootstrap']
del rm[3]
print(rm)

#clear() method clears the list content but still list will be there with empty.
rm = ['python', 'html', 'css', 'bootstrap']
rm.clear()
print(rm)