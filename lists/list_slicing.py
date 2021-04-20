# list slicing 
amazon_cart = [
    'iphone11',
    'laptop',
    'smart watch',
    'monitor',
    'computer table'
]

print(amazon_cart[1]) # laptop
print(amazon_cart[0:3]) # ['iphone11', 'laptop', 'smart watch']
print(amazon_cart[:]) # ['iphone11', 'laptop', 'smart watch', 'monitor', 'computer table']
print(amazon_cart[0::1])

# lists are mutable
amazon_cart[0] = 'iphone_12'
print(amazon_cart)

# with list slicing we are copying a list  
creating_new_list = amazon_cart[0:2]
print(creating_new_list)

# changing values from one range to another range with the help of list slicing.
amazon_cart[0:2] = ['iphone 13', 'mackbook' ]
print(amazon_cart)

amazon_cart[0:6] = ['iphone 13', 'mackbook']
print(amazon_cart)
print(len(amazon_cart))


