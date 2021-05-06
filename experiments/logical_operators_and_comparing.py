'''

When we execute the program print('a' > 'b') it gives us the answer False.

When we execute the program print('a' > 'A') it gives us the answer True.

Please help me with a detailed explanation.

'''
# when comparing characters using < or > it will convert into integer.
# so basically, it will return the result based on ascii table.

print('a' > 'b') # ascii value of a is 97 and b is 98 
print(97 > 98) # False
print('a' > 'A') # ascii value of a is 97 and A is 65
print(97>65) # True

