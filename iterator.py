

'''
Python iterator class tips
'''
a = [1,2,3]
b = iter(a)
print(next(b)) # 1
print(next(b)) # 2
print(next(b)) # 3

# print(next(b)) # ERROR since we run out of element

# Do this instead
print(next(b, None))



