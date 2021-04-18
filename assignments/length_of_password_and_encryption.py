user_name = input("enter a username:- ")
password = input("enter password:- ")

length_of_the_password = len(password) # getting the length of the password
encoding_password = length_of_the_password * '*' # muliplying the length of the password with string '*'

print(f' the username is: {user_name} and password is {encoding_password}, finally length of the password {length_of_the_password}')


