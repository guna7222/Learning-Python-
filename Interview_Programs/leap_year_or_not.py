'''
Write a python program to check wheather a given year is leap year or not?
'''

def leap_year(year): # def keyword is used to define a function
  if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("Yes, it is a Leap Year! ")
  else:
    print("It's not a Leap Year!")

year = int(input('Enter a Year to check Leap Year or Not:- '))
leap_year(year) # function calling
  
