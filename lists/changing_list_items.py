
# changing list items 
comp_languages = ['python', 'go', 'java', 'sql']
comp_languages[2] = 'c'
print(comp_languages)

# changing two items in a list 
comp_languages = ['python', 'go', 'java', 'sql']
comp_languages[0:2] = 'c', 'r' # 2 exclusive 
print(comp_languages)

# insert() method inserts the item into specified index
comp_languages = ['python', 'go', 'java', 'sql']
comp_languages.insert(4, 'aws')
print(comp_languages)

#Example
thislist = ['aws', 'docker', 'mysql']
thislist[1:3] = ['Docker'] 
'''
If you insert less items than you replace, the new items will be inserted where you specified,
and the remaining items will move accordingly:
'''
print(thislist)

# Another Example
thislist = ['aws', 'docker', 'mysql', 'go']
thislist[1:2] = ['Docker']
print(thislist)

# Example
thislist = ['aws', 'docker', 'mysql', 'go']
thislist[1] = ['Docker']
print(thislist)

