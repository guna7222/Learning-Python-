# palindrome 

name = input("enter a name:- ")
if name == name[::-1]: # used to reverse a string 
    print("palindrome")
else:
    print("not a palindrome")
    
    
# palindrome using functions

def palindrome(string):
    if string == string[::-1]:
        print(f' {string} palindrome')
    else:
        print(f' {string} not a palindrome')
        
string = input('enter a string:- ')
palindrome(string)
