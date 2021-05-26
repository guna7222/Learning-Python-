'''
Print multiplication table for given number

'''

def multiplication(table, times): 
    for i in range(1, times + 1):
        print(table, 'x', i, '=', table*i)
    
    

table = int(input('Enter a table:- '))
times = int(input('Enter times:- ')) 
multiplication(table, times)

    
    
