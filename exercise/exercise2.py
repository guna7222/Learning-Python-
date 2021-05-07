# logical operators exercise:- 
is_magician = True
is_expert = False

# check if magician and expert : 'you  are a master magician'
if is_magician and is_expert:
    print('you are a master magicain')

# check if magician but not expert: 'at least you are getting there'
elif is_magician == True and is_expert != True:
    print('at least you are getting there')

# if you are not'a magician: " you need magic powers:"
elif is_magician == False:
    print('you need magic powers')
