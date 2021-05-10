user_input = int(input('enter a number:- '))
if user_input > 1:
    for i in range(2, user_input):
        if (user_input % i)==0:
            print('it is not a prime number')
            break
        
    else:
        print('it is a prime number')
        
else:
    print('enter a valid number')
