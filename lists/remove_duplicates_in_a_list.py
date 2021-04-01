# Remove duplicates in a string 
duplicate_values = ['Python', 'Go', 'Django', 'Python', 'Go']
unique = []
for i in duplicate_values:
    if i not in unique:
        unique.append(i)
        
unique.sort(key=None, reverse=False)
print(unique)