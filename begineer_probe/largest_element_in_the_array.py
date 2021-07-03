'''
Python Program to find largest element in an array

'''

def largest_element_in_the_array(arr):
     arr.sort(reverse = True)
     print(f' The largest number in the arr is:- {arr[0]}')


largest_element_in_the_array([10, 20, 100, 1000, 10000])
    

# different approach 

arr = [ 1, 10, 20, 90, 5, 8 ]
print(max(arr)) # max function 


# another approach

arr1 = [ 1, 10, 20, 90, 5, 8, 100 ]
max = arr1[0]
for i in arr1:
    if i > max:
        max = i
print(f' The largest number in the array is:- {max}')

# Another way
# Largest element in the array
elements_len = int(input('Enter elements:- '))
array = []
for i in range(1, elements_len+1):
    num = int(input('enter numbers:- '))
    array.append(num)
    largest_ele = max(array)
print(largest_ele)
    
    
