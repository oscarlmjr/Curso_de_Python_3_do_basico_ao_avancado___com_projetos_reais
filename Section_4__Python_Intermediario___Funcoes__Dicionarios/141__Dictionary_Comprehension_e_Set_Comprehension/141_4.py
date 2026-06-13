
lista = [
	('a', 'valor a'),
	('b', 'valor a'),
	('b', 'valor a'),
]

dc = {chave: valor for chave, valor in lista}

print(dc, type(dc), '\n')

print(dict(dc), type(dict(dc)), '\n')

s1 = ({'a': 'valor a', 'b': 'valor a'})
print(s1, type(s1), '\n')

s1 = {2 ** i for i in range(10)}
print(s1, type(s1))
