# Local variable 

'''
Variables declared inside a function is known as local variable.
Local variable are not accessible by outside of the function.
''' 
def function():
	course = 'Python full stack developer' # local variable  
	print(course)

function()

'''
when you access a local variable outside of the function, it will throw an
Error
'''
#print(course)
'''
There is a way to access a local variable in global space using 
global keyword
'''
#example
def function():
	global local_variable #Global keyword
	local_variable = 'Github'
	print("learned github")
function()
print(local_variable) # Accessing local variable outside of the function.
