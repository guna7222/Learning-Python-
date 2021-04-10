# palindrome 

name = input("enter a name:- ")
if name == name[::-1]: # used to reverse a string 
    print("palindrome")
else:
    print("not a palindrome")