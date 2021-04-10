smallest_number = [12, 34, 89, 100, 7 , 1]
position = smallest_number[0]
for i in smallest_number:
    if i < position:
        position = i
        
print(position)
