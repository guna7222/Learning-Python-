# skiping 'name' key and printing remaining all the keys.
this_dict = {"name":"gunasekhar R", 'age':23, 'door_no': 20.3, 'boo':True}
for i in this_dict:
    if i == 'name':
        continue 
    print(i)
    
    
