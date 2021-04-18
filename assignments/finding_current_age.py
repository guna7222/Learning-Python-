import datetime # importing datetime module 


birth_year = int(input('what year you were born? '))
present_year = datetime.datetime.now().year
age = present_year - birth_year
print(age)


