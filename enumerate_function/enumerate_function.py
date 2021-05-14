'''

enumerate() function assigns an index to each item in an iterable objects.

'''
from builtins import enumerate
import string

string = 'python packages are namespaces that contains multipule modules'
for i, j in enumerate(string):
    print(i, j)