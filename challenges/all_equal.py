'''
Define a function named all_equal that takes a list and checks whether all elements in the list are the same.

For example, calling all_equal([1, 1, 1]) should return True.

'''

# Example

def all_equal(lists):
    return all(i == lists[0] for i in lists)
    
print(all_equal([1,1,1]))
