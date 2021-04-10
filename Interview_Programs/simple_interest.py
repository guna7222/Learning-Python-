# simple interest 
from builtins import input
principal = int(input("Enter a principal amount:- "))
rate = int(input("enter a rate of interest:- "))
time = int(input("enter a time duration:- "))
final_amount = principal*rate*time/100 #TIP:-Simple interest formula PTR/100
print(final_amount)