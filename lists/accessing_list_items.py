#accessing list items 
friends = ["guna", "Thrilok", "Hemanth", "Chandu"]
print(friends)
print(friends[0]) # the first item has a index [0]

# Negative indexing starts from -1
friends = ["guna", "Thrilok", "Hemanth", "Chandu"]
print(friends)
print(friends[-2]) 

#range 
friends = ["guna", "Thrilok", "Hemanth", "Chandu"]
print(friends[1:])

# check if item exists
friends = ["guna", "Thrilok", "Hemanth", "Chandu"]
if "guna" in friends:
  print("yeah! he is avaliable")

# range of negative indexes 
friends = ["guna", "Thrilok", "Hemanth", "Chandu"]
print(friends[-3:-1]) # -1 is excluded 


