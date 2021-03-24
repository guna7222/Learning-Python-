# Global Variable 
''' A variable is created outside of the function is know as global variable.
Global variable can be used by everyone inside and outside of the function.
'''

#Example 
name = 'learn'
def function():
	print('local variable')

function()
print(name) # Global variable

# Global variable inside the function 

name = 'learn'
def function():
	print(name)

function()
