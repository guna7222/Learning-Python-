'''

Write a Python program to calculate compound interest?
Formula to calculate compound interest annually is given by:
Compound Interest = P(1 + R/100)r
Where,
P is principle amount
R is the rate and
T is the time span

'''

def compound_interest(p, r, t):
    return p * (1+r/100) * r
    
    
print(compound_interest(10000, 3, 5))