'''
Min-maxing
Define a function named largest_difference that takes a list of numbers as its only parameter.

Your function should compute and return the difference between the largest and smallest number in the list.

For example, the call largest_difference([1, 2, 3]) should return 2 because 3 - 1 is 2.

You may assume that no numbers are smaller or larger than -100 and 100.

'''
# Solution
def largest_difference(ls):
    for i in ls:
        largest_number = max(ls)
        smallest_number = min(ls)
        difference = largest_number - smallest_number
    return difference
    
    
print(largest_difference([1,2,3]))
