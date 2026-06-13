variavel = ['Luiz otavio', 'Joãozinho', 'Maria']

for valor in variavel:
	if valor.lower().startswith('j'):
		continue
	print(valor)
else:
	print('Não existe uma palavra que começa com J.')
