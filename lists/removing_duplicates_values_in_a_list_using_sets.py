# Here is Another way of removing duplicates items in a list 
lis = ['apple', 'banana', 'mango', 'pineapple', 'banana', 'apple']
print(lis)
convertion = set(lis) # converting list to set to remove duplicate values
print(convertion)
lis = list(convertion) # again converting from set to list
print(lis)