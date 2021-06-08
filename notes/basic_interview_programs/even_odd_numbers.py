'''
Even or odd number
even numbers are like 0,2,4,etc.,
odd numbers are like 1,3,5 and etc.,

'''
def even_odd(number):
    if (number % 2) == 0:
        return 'Even number'
    else:
        return 'Odd number'
        
number = int(input('enter a number:- '))
print(even_odd(number))

