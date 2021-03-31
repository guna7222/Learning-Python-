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
