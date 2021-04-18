import datetime # importing datetime module 


birth_year = int(input('what year you were born? '))
present_year = datetime.datetime.now().year
age = present_year - birth_year
print(age)


# same thing doing with functions

import datetime

def current_age(age):
  dynamic_year = datetime.datetime.now().year
  age = dynamic_year - age
  print(age)


age = int(input('enter your current age:- '))
current_age(age)
