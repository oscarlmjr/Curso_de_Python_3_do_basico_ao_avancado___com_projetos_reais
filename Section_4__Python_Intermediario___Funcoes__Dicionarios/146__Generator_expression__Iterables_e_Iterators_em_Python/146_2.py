# Generator expression, Iterables e Iterators em Python

lista = [n for n in range(10)]
iterator = lista.__iter__()

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator), '\n')


iterator = iter(lista)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
