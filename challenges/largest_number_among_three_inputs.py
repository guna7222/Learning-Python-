# Python program to find the largest number among the three input numbers

num1 = int(input('enter a first number:- '))
num2 = int(input('enter a second number:- '))
num3 = int(input('enter a thrird number:- '))

if (num1>=num2) and (num1>=num3):
    largest_number = num1
elif (num2>=num1) and (num2>=num3):
    largest_number = num2
else:
    largest_number = num3

print(f' The largest number among there numbers is: {largest_number} ')
