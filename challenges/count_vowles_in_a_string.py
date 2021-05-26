'''
count how many vowles in a string

'''
        
def vowles(string):
    count = 0
    vowles = ['a', 'e', 'i', 'o', 'u']
    for i in string:
        if i in vowles:
            count = count+1
            print(count)
    
    
vowles('Hello Python')