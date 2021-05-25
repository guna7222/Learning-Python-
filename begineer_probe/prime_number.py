'''

Program to find if a given number is prime?

A number that is divisible by 1 and itself is called prime number example: 7

'''

def prime_number(number): # def keyword is used to define a function.
    if number > 1:
        for i in range(2, number):
            if (number % i) ==0:
                return f' {number} is not a prime number'
                break
        else:
            return f' {number} is a prime number'
    else:
        return 'enter a number greater than 1'
    
    
print(prime_number(7))