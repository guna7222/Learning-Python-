# Positive number or Negative number 
num = int(input("Enter a number to check positive or Negative:- "))
if num < 0:
    print("It is a Negative number")
elif num == 0:
    print("0 is a positive number")
else:
    print(f'{num} number is positive number')
    
    
    
    
# positive or negative number using functions

def positive_negative(num):
    if num < 0:
        print(f'{num} is negative number')
    else:
        print(f'{num} is positive number')
        
        
num = int(input('enter a number:- '))
positive_negative(num)
