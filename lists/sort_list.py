'''
Sort method is used to sort the list objects into alphabetical order, 
ascending order is the default oder.
'''
from audioop import reverse

companies = ['Apple', 'zebra', 'cisco', 'amazon', 'google', 'samsung', 'dell', 'cts']
companies.sort()
print(companies)

# sorting in descending order
# we have to use keyword argument for descending order reverse = True

companies = ['Apple', 'zebra', 'cisco', 'amazon', 'google', 'samsung', 'dell', 'cts']
companies.sort(reverse = True) # keyword argument 
print(companies)