'''
Count words in a sentence? 

'''

def count_sentence():
    sentence = input('enter a sentence:- ')
    words = sentence.split()
    print(len(words))
    
    
count_sentence()