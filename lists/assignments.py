'''
write a python program to check values that are present in the both of the lists
example: 
lis = ["guna", "sekhar", 22]
lis2 = ["guna", 25, "prabhas"]

OUTPUT:-
final_list = ['guna']
'''

lis = ["guna", "sekhar", 22]
lis2 = ["guna", 25, "prabhas"]
convert = set(lis)
convert1 = set(lis2)
print(convert)
print(convert1)
result = convert.intersection(convert1)
print(result)
final_list = list(result)
print(final_list)
