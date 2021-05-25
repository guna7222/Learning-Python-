'''
a way to remove the last object from a list?

we can remove the last object from a list using pop() method without index position.
'''

ls = list(range(1, 10))
print(ls)
ls.pop() # pop(-1)  method removes last item if index value does'nt specify.
print(ls)


# using functions

def remove_last_item(ls):
    print(ls)
    ls.pop()
    print(ls)
    
remove_last_item([10, 20, 30, 100])