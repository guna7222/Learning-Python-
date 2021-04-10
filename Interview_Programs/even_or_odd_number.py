from builtins import input

user_input = int(input("Enter a number to check whether a number is Even or Odd"))
if user_input%2 == 0:
    print(f"Yes, {user_input} it is a Even number ")
else:
    print(f"It {user_input} is a Odd number ")
    