

'''
Python itertools
'''

import itertools


a = [i for i in range(100)]

iter_a = iter(a)

print("")
print(f'--------- This will do next operation up to 50 elements')

for x in itertools.islice(iter_a,50):
    print(x)

print("")
print(f'---------This will print out an element starting after the 50 elements')
for x in iter_a:
    print(x)

