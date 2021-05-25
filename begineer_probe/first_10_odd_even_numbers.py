'''
Program to print first 10 odd/even numbers?

'''

def first_10_odd_even_numbers(numbers):
    for i in range(1, numbers+1):
        if (i%2)==0:
            print(f'{i} is even number')
            print(' ')
        else:
            print(f'{i} is odd number')
            print(' ')
            

first_10_odd_even_numbers(10)