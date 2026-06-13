# object acima
Foo = type('Foo', (object,), {})
f = Foo()

# print(isinstance(f, Foo))
print(type(f))
print(type(Foo))
