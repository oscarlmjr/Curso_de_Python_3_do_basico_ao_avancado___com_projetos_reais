"""
Listas em Python
fatiamento
append, insert, pop, del, clear, extend
min, max
range
"""
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l1.extend(l2)
print(l1)
print(l2)
l1.extend('rua')  # apenas para string
l1.append(7)  # para string ou int
l2.insert(1, 'casa')  # add 1 índice a + na posição indicada.
print(l1)
print(l2)
print(l2[1])
l1.pop(5)
l1.pop()
print(l1)
