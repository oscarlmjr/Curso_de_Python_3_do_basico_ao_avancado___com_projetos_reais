# Generator expression, Iterables e Iterators em Python
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iterable.__iter__()
# iterator = iterable.__next__   # AttributeError: 'list' object has no attribute '__next__'.

print(next(iter(iterable)))
print(next(iter(iterable)))
print(next(iter(iterable)), '\n')


iterable = ['Eu', 'Tenho', 'iter(iterable)']
iterator = iter(iterable)

print(next(iter(iterator)))
print(next(iter(iterator)))
print(next(iter(iterator)))
