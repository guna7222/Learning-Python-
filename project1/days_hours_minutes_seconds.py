days = int(input("enter no of days:- ")) # Taking input from user for number of days 
hours =  days*24 # formula for converting days = hours 
minutes = hours*60 # formula for converting days = minutes
seconds = minutes*60 # formula for converting days = seconds
print(f'for {days} days {hours} hours ') # formated string used to combine string and interger. 
print(f'for {days} days {minutes} minutes')
print(f'for {days} days {seconds} seconds')
