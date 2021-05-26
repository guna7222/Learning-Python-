'''
how to extract every alternate letters from a string in python?

'''
def extract_alternative_letters(string):
     print(string[::2])


extract_alternative_letters('Hello World')


# another way of doing same

def alternative_letters(string):
    empty_string = ''
    for i in range(0, len(string)):
        if (i % 2) == 0:
            empty_string = empty_string + string[i]
            
    print(empty_string)
    
alternative_letters('Hello World')