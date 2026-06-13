# Generator expression, Iterables e Iterators em Python
iterable = ['Eu', 'Tenho', 'iterable.__iter__']
iterator = iterable.__iter__()
# iterator = iterable.__next__   # AttributeError: 'list' object has no attribute '__next__'.

print(iterator)
print(iterable.__iter__(), '\n')

print(next(iterator))
print(next(iterator))
print(next(iterator), '\n')
# print(next(iterator))   # StopIteration


iterable = ['Eu', 'Tenho', 'iter(iterable)']
iterator = iter(iterable)

print(next(iterator))
print(next(iterator))
print(next(iterator), '\n')
# print(next(iterator))   # StopIteration
