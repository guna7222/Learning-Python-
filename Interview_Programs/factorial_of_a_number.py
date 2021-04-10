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