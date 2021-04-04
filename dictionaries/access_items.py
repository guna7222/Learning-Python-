# accessing items 
this_dict = {"name":"gunasekhar R", 'age':23, 'door_no': 20.3, 'boo':True}
print(this_dict["name"])

#Example2
this_dict = {"name":"gunasekhar R", 'age':23, 'door_no': 20.3, 'boo':True}
access = this_dict["age"]
print(access)

# get is the another method of accessing items in the dict.
this_dict = {"name":"gunasekhar R", 'age':23, 'door_no': 20.3, 'boo':True}
access = this_dict.get('boo')
print(access)

# keys method returns a list of all the keys in the dict. 
this_dict = {"name":"gunasekhar R", 'age':23, 'door_no': 20.3, 'boo':True}
key = this_dict.keys()
print(key)
this_dict["mobile_no"] = 82923
print(this_dict)

