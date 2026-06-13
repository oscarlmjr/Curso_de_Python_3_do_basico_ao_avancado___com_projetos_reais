"""
Listas em Python
fatiamento
append, insert, pop, del, clear, extend
min, max
range
"""
#	 0  1  2  3  4  5  6  7  8
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del(l2[3:5])
del(l2[0])
print(l2, type(l2))
print(max(l2))
print(min(l2))
l2 = range(1, 5)
print(l2, type(l2))
for valor in l2:
	print(valor)
l2 = list(range(1, 10))
print(l2, type(l2))
l2 = list(range(0, 48, 8))
print(l2)
l2 = list[1, 10]
print(l2, type(l2))
