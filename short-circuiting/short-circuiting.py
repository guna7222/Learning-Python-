# Yes! python does have short-circuiting.
'''
and
or
'''
is_best_friend =  False
is_friend = True
 if is_best_friend and is_friend: # here is_best_friend is False so it will short-circuit it won't check is_friend because is_best_friend is false.
  print("yes condition is True")
else:
  print('condition is False')
