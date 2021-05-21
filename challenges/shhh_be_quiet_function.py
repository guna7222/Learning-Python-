'''
Shhh Be Quiet Function
Write a function that removes all capitals letters from a sentence except the first letter, put quotation marks around the sentence and add ", whispered Edabit." at the end.

Examples
shhh("HI THERE!") ➞ '"Hi there!", whispered Edabit.'

shhh("tHaT'S Pretty awesOme") ➞ '"That's pretty awesome", whispered Edabit.'

shhh("") ➞ '"", whispered Edabit.'
Notes
Don't forget to surround the original string with double quotation marks "".
'''
# solution using f string

def shhh(txt):
	return f'"{txt.capitalize()}", whispered Edabit.'
print(shhh("HI THERE!"))

# solution using format method

def shhh(txt):
	return '"{}", whispered Edabit.'.format(txt.capitalize() )
print(shhh("HI THERE!"))
