'''
Sum of an array of numbers?

'''
from pip._internal.utils import unpacking

def sum_of_array(arr):
    return sum(arr) # sum function returns a number, the sum of all items in an iterable objects.


print(sum_of_array([10, 20, 30, 50]))


'''

sum of array using unpacking

unpacking:- When you have a collection of items in a list, tuple and etc., you can extract them

into a variable using unpacking. This is called unpacking. 

'''
array = [1,2,3,4,5,6,7,8,9]
a,b,c,d,e,f,g,h,i, = array
print(a+b+c+d+e+f+g+h+i)


# Taking range from users

def sum_arr():
    lis = []
    count = int(input('range of values:- '))
    for i in range(1, count + 1):
        values = int(input('enter values:- '))
        lis.append(values)
        print(f'sum of {lis} is:- ', sum(lis))
        
        
sum_arr()

# sum array without using sum() function

def sum(arr):
    sum = 0
    for i in arr:
        sum = sum + i
    print(sum)
        
sum([10, 20, 20])
    
    
