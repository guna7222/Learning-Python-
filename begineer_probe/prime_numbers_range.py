'''
Program to print prime numbers between given range?

'''

def prime_range(start, end):
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
                
            else:
                print(num)
                
        else:
            print('enter number greater than 1')
            
   
prime_range(10, 50)         
