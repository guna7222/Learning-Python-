'''
Default Mood
Create a function that takes in a current mood and return a sentence in the following format: "Today, I am feeling {mood}". However, if no argument is passed, return "Today, I am feeling neutral".

Examples
mood_today("happy") ➞ "Today, I am feeling happy"

mood_today("sad") ➞ "Today, I am feeling sad"

mood_today() ➞ "Today, I am feeling neutral"
Notes
Check the Resources tab for some helpful information.

'''
# solution

def mood_today(mood ='neutral'): # we can assign a default argument value
	return "Today, I am feeling {}".format(mood)
	
	
print(mood_today())
	
