# Sets
# A Set is a collection which is unordered, un-indexed, and it won't allow duplicate values
# set uses curly braces {}
from builtins import set
from test.test_enum import Fruit
fruits = {"apple","mango", 1, 20.2, False}
print(fruits)

#Duplicate values will be ignored 
fruits = {"apple","mango", 'mango', 1, 1}
print(fruits) #unordered

#Get a length of the set 
fruits = {"apple","mango", 'mango', 1, 1}
print(len(fruits))

# set can have different data types.
fruits = {"apple","mango", 'mango', 1, 20.0, True}
print(fruits)

# set constructor 
fruits = set(("apple","mango", 'mango', 1, 1))
print(fruits)
