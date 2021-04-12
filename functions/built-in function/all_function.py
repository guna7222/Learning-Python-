# all() only one parameter
# all(iterable)
# all(list, tuple, dict, set)
# The all() function returns True if all elements in the given iterable are true. If not, it returns False.
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

#sets()
st = {1,2,3,0}
print(all(st))


#tuple()
tp = (1,2,3,4,5)
print(all(tp))

# dict()
dt = {
    0:'value1',
    1:'value2'
}
print(all(dt))
