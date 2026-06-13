# count é um iterador sem fim (itertools)
from itertools import count

c1 = count(8, 8)
r1 = range(10, 15)

print(next(c1))
print(next(c1), '\n')

print(r1)
print(range(10))
print(range(10, 15), '\n')

for r in r1:
	print(r)

print('')

print('c1', hasattr(c1, '__iter__'))
print('c1', hasattr(c1, '__next__'))
print('r1', hasattr(r1, '__iter__'))
print('r1', hasattr(r1, '__next__'), '\n')
