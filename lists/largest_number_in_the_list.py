# finding the largest number in the list
largest_number = [12, 22, 30, 31, 100]
position = largest_number[0]
for i in largest_number:
    if i>position:
        position=i
print(f'The largest value in the list is:- {position} ')