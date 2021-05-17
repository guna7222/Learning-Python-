'''
Boolean and
Define a function named triple_and that takes three parameters and returns True only if they are all True and False otherwise.

'''

# solution.
def triple_and(first, second, third):
    if first == True and second == True and third == True:
        return True
    else:
        return False
    
print(triple_and(12, 90, 98))
