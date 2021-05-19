sub_array = []
no_of_types = int(input('enter a number:- '))
for i in range(1, no_of_types+1):
    numbers = int(input('enter a number:- '))
    sub_array.append(numbers)

print(sum(sub_array))
