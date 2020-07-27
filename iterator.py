

'''
Python iterator class tips
'''

### Tip 1 - Next one in the iterator
a = [1,2,3]
b = iter(a)
print(next(b)) # 1
print(next(b)) # 2
print(next(b)) # 3

# print(next(b)) # ERROR since we run out of element

# Do this instead
print(next(b, None))



### Tip 2 - Iterate through dictionary

# Dictionary key can be accessed by iterator and next command.
A = {str(i):chr(i) for i in range(10)}
print(iter(A))
for _ in range(10):
    the_next_key = next(iter(A))
    del  A[the_next_key]







