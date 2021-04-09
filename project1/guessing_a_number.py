secret_number = 8
count = 0
chances = 3
while count < chances:
    user_input = int(input("enter a secret number:- "))
    count = count+1
    
    if user_input == secret_number:
        print("Wonderful you won the game. ")
        break
    elif user_input != secret_number:
        if count == 1:
            print("you have two more chances")
        elif count == 2:
            print("you have last chance")
            
else:
    print("sorry try again")