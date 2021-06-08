'''
Factorial of a number
'''
import math

def factorial(number):
    return math.factorial(number)
    
number = int(input('enter a number:- '))
print(factorial(number))

# Another method

def factorial(num):
    fact = 1
    if num < 0:
        print("Factorial doesn't exits for negative numbers")
    elif num == 0:
            print('factorial of 0 is 1')
    else:
        for i in range(1, num+1):
            fact = fact*i
        print(fact)
        
num = int(input('enter a number:- '))
factorial(num)
