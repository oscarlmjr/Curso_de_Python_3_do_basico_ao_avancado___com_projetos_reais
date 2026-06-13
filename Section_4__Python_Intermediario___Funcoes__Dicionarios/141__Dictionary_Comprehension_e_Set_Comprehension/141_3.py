
produto = {
	'nome': 'Caneta Azul',
	'preco': 2.5,
	'categoria': 'Escritório',
}

dc = {
	chave: valor
	if isinstance(valor, (int, float, bool)) else valor.upper()
	for chave, valor
	in produto.items()
	if chave != 'categoria'
}

print(dc, '\n')
