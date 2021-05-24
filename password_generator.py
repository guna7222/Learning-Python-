# password generator 


import random

lower_case = 'abcdefghijklmnopqrstuvwxyz'
upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '*#$%&()_@.;'

combine_all = lower_case + upper_case + numbers + symbols
length = 12
password = ''.join(random.sample(combine_all, length)) # sample method syntax random.sample(sequence, k) k Required. The size of the returned list
print(password)
