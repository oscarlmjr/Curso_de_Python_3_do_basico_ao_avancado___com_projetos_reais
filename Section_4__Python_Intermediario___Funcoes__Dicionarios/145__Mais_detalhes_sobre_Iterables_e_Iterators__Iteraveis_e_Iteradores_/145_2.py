# Generator expression, Iterables e Iterators em Python
iterable = ['Eu', 'Tenho', 'iterable.__iter__']
iterator = iterable.__iter__()  # tem __iter__ e __next__
# iterator = iterable.__next__   # AttributeError: 'list' object has no attribute '__next__'.

print(next(iterable.__iter__()))
print(next(iterable.__iter__()), '\n')

iterator = iter(iterable)

print(next(iterator.__iter__()))
print(next(iterator.__iter__()))
print(next(iterator.__iter__()), '\n')

iterable = ['Eu', 'Tenho', 'iter(iterable)']
iterator = iter(iterable)

print(next(iterator.__iter__()))
print(next(iterator.__iter__()))
print(next(iterator.__iter__()))
