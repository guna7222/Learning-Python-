fnum = int(input("enter a number to check its factorial:- "))
factorial = 1
if fnum<0:
    print("factorial does't exits negative numbers ")
elif fnum == 0:
    print("The factorial of 0 is 1 ")
else:
    for i in range(1, fnum+1):
        factorial = factorial * i
    print(factorial)
    
    
    
    
# factorial of a number using return 
def factorial(number):
    fact = 1
   
    if number <= 0:
        return 'enter positive number'
    elif number == 1:
        return 'Factorial of 1 is 1'
    else:
        for i in range(1, number+1):
            fact = fact*i
        return fact
            
number = int(input('enter a number:- '))
print(factorial(number))
