'''
Convert Hours into Seconds
Write a function that converts hours into seconds.

Examples
how_many_seconds(2) ➞ 7200

how_many_seconds(10) ➞ 36000

how_many_seconds(24) ➞ 86400
Notes
60 seconds in a minute, 60 minutes in an hour
Don't forget to return your answer.

'''
# solution

def how_many_seconds(hours):
	seconds = 60 # per minutes = 60 seconds 
	minutes = 60 # 60 minutes per hour
	return hours * minutes * seconds
	
print(how_many_seconds(2))
