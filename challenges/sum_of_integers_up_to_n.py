'''
Sum of Integers Up To n (integersums.py)

Write a function, add_it_up(), that takes a single integer as input and returns the sum of the integers from zero to the 

input parameter. The function should return 0 if a non-integer is passed in.

'''
# Solution

def add_it_up(n):
    sum = 0
    for i in range(n+1):
        sum = sum + i
        
    return sum

add_it_up(5)
        
