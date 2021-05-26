''' 
Keyword arguments vs Positional arguments

Keyword arguments are bad practise. 
'''

def greetins(name, age):
    print(f'my name is:{name} and age {age}')
    
# positional arguments  
greetins('Gunasekhar', 22) # These are called positional arguments

# keyword arguments
greetins(age = 22, name = 'Gunasekhar')

# Default parameters:-

def greetings(name = 'gunasekhar', age = 23): # default arguments 
    print(f'my name is:{name} and age {age}')
    
    
greetings()
     
