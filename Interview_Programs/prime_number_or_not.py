# a number that is divisible only by itself Example:-(2,3,5,7) 
user_input = int(input("enter a number:- "))
if user_input > 1:
    for i in range(2, user_input):
        if (user_input % i)==0:
            print("it is not a prime number! ")
        else:
            print(f"{user_input} is a prime number! ")
            
else:
    print("it is not a prime number !")