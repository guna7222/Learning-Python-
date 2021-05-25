# Program to find odd/even number?

def odd_or_even(num):
    if num % 2 == 0:
        return f'{num} is even number!'
    else:
        return f'{num} is odd number! '
    

print(odd_or_even(4))