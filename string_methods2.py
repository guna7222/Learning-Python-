# string methods
# .title()
# converts first character of each word into uppercase.
txt = "welcome to my world"
print(txt.title())

# .isupper returns True or False.
txt = "welcome to my world"
print(txt.isupper())

# .islower also returns True or False.
txt = "welcome to my world"
print(txt.islower())

#isalpha (Returns True if all the character's in the string are alphabets(a-z).
txt = "welcome to my world"
print(txt.isalpha())

#isnumeric returns True if all the character's in the string numbers.
txt = "154615"
print(txt.isnumeric())

#endswith return's True if the specified value present at the ending of the string.
txt = "so, this is the example about endswith method."
print(txt.endswith('.'))

#startswith returns True if the specified value present at the begining of the string.
txt = "so, this is the example about endswith method."
print(txt.startswith('s'))
