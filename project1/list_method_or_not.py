# Write a program to check whether user_input method exists in lists or not?
list_methods = ['append', 'insert', 'extend', 'pop', 'remove', 'copy', 'count', 'index', 'clear', 'sort', 'reverse']

user_input = input("enter a method to check whether it belongs to list or not:- ")
for i in list_methods: # in operator is used to check certain phrase or character is present in a string 
    if user_input in list_methods:
        print("yes! it is a list method ")
        break # break statement stops the loop even if the condition is True. 
else:
    print("Not a list method ")
