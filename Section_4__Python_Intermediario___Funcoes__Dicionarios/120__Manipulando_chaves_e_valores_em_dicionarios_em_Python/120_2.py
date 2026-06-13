
pessoa = {}

pessoa['nome'] = 'Luiz Otávio'
print(pessoa)
print(pessoa['nome'], '\n')

if pessoa.get('sobrenome') is None:
	pessoa['sobrenome'] = 'Miranda'
	print(pessoa)
	print(pessoa['sobrenome'])
else:
	print(pessoa['sobrenome'])
