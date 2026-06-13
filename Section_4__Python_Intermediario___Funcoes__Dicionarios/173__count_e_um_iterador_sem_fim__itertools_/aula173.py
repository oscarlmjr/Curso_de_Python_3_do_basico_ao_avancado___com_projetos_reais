# count é um iterador sem fim (itertools)
from itertools import count

c1 = count()
r1 = range(5)

print('c1', hasattr(c1, '__iter__'))
print('c1', hasattr(c1, '__next__'))
print('r1', hasattr(r1, '__iter__'))
print('r1', hasattr(r1, '__next__'), '\n')


print('count')
for i in c1:
	if i > 5:
		break
	print(i)

print('\nrange')
for i in r1:
	print(i)
