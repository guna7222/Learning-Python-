# print duplicate values in a list 

# solution 
lis = ['a', 'b', 'a', 'c', 'd', 'd']
duplicates = []
for i in lis:
    if i not in duplicates:
        duplicates.append(i)
        
    else:
        print(i, end = '')
        
        

# finding duplicates in a list using different approach
lis = ['a', 'b', 'a', 'e']
duplicates = []
for i in lis:
    if lis.count(i)>1:
        duplicates.append(i)
        print(duplicates)
        
