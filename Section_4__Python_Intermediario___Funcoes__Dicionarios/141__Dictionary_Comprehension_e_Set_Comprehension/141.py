# Dictionary Comprehension e Set Comprehension

produto = {
	'nome': 'Caneta Azul',
	'preco': 2.5,
	'categoria': 'Escritório',
}

print(produto.items(), '\n')

for chave, valor in produto.items():
	print(chave, valor)

print()

dc = {chave: valor for chave, valor in produto.items()}

print(dc, '\n')
