'''
Taking multiple input from users and spliting the input by using split() method,
at final printing the stored data.
'''
store = []

weapons = input("enter a multiple weapon names by comma separated:- ") # split() methods converts the sttring into list.
weapons.split(',')
greetings = input("enter a multiple greetings names by comma separated:- " )
greetings.split(',')
friends = input("enter a multiple friends names by comma separated:- " )
friends.split(',')

store.append({
    'weapons': weapons,
    'greetings':greetings,
    'friends':friends
})


print(store)
