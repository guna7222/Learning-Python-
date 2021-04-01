# adding list items 
'''
append() method
To add an item to the end of the list by using append method.
'''
from maxlist import another
from builtins import print

thislist = ["cloud", 'devops', 'github']
thislist.append('Python full stack') #append method appends the item into end of the list
print(thislist)

# insert() method is used to add the item at the specified index
thislist = ["cloud", 'devops', 'github']
thislist.insert(1, 'java')
print(thislist)

# extend method is used to append the another list elements to current list 
thislist = ['cloud', 'devops', 'github']
anotherlist = ['python', 'database']
thislist.extend(anotherlist)
print(thislist)

# a Method is a function that belongs to an object.
