# lists 
# all() built-in function 
# all() function returns True if any element iteratable is True!
x = [1,2,3,4,5]
print(all(x))
# Tip:- all values are True, True 

x = [0, False]
print(all(x))
# Tip:- all values are False, False

x = []
print(all(x))
# Tip:- all values are empty, True

x = [1, False, 0]
print(all(x))
# Tip:- one value True and remaining False, False 

x = [1,2,3,4,5,0]
print(all(x))
# Tip:- all values are True and one is False, False

# strings
st = 'Guido van Rossum 1991'
name = all(st)
print(name)

st = '0 False'
result = all(st) # returns True because 0 and False are strings
print(result)

st = ' ' 
empty_string = all(st)
print(empty_string)


