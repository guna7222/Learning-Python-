days = int(input("enter no of days:- ")) # Taking input from user for number of days 
hours =  days*24 # formula for converting days = hours 
minutes = hours*60 # formula for converting days = minutes
seconds = minutes*60 # formula for converting days = seconds
print(f'for {days} days {hours} hours ') # formated string used to combine string and interger. 
print(f'for {days} days {minutes} minutes')
print(f'for {days} days {seconds} seconds')


# new version  
days = int(input("enter no of days:- ")) # Taking input from user for number of days 

avaliable_menu = input(" \n enter 'h' for hours or enter 'm' for minutes or enter 's' for seconds:- ")

def hours():
    print(days * 24)
    
def minutes():
    print(days*24*60)
    
def seconds():
    print(days*24*60*60)

while avaliable_menu != 'q':
    if avaliable_menu == 'h':
        hours()
    
    elif avaliable_menu == 'm':
        minutes()
    
    elif avaliable_menu == 's':
        seconds()
    
    else:
        print("Please select provided options ")
        
    avaliable_menu = input(" enter 'h' for hours or enter 'm' for minutes or enter 's' for seconds:- ")   


