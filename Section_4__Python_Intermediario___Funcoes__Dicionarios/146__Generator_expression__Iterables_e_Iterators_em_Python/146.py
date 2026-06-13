# Generator expression, Iterables e Iterators em Python
import sys


lista = [n for n in range(1000000)]
generator = (n for n in range(1000000))   # tupla gera um generator

print(generator, type(generator), '\n')

# for n in generator:   # desencapsula
#	 print(n)

print(sys.getsizeof(lista))   # em bytes
print(sys.getsizeof(generator), '\n')

# print(next(lista))   # TypeError: 'list' object is not an iterator
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
