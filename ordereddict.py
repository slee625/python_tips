'''
Ordered dictionary is pretty useful when we implement Queue in dictionary form
'''


import collections

Q = collections.OrderedDict()


A = [('Foreast Gump','1988'),('Titanic','1992'),('Matrix','2003'),('Avengers I','2013'),('Benet','2020')]

for x in A:
    Q[x[0]] = x[1]
    print(Q)


# Pop the first element (FIFO) that was inserted to the dictionary
print(Q)                #  OrderedDict([('Foreast Gump', '1988'), ('Titanic', '1992'), ('Matrix', '2003'), ('Avengers I', '2013'), ('Benet', '2020')])
Q.popitem(last = False) 
print(Q)                #  OrderedDict([                          ('Titanic', '1992'), ('Matrix', '2003'), ('Avengers I', '2013'), ('Benet', '2020')])

# Pop (delete) the specified key
print(Q)  # OrderedDict([('Titanic', '1992'), ('Matrix', '2003'), ('Avengers I', '2013'), ('Benet', '2020')])
Q.pop('Matrix')
print(Q)  # OrderedDict([('Titanic', '1992'),                   , ('Avengers I', '2013'), ('Benet', '2020')])