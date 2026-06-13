"""
enumerate - enumera iteráveis (índices)
"""
# [(0, 'Maria'), (1, 'Helena'), (2, 'João')]
lista = ['Maria', 'Helena']
lista.append('João')

lista_enumerada = enumerate(lista)
print(lista_enumerada, '\n')

print(next(lista_enumerada))
print(next(lista_enumerada))
print(next(lista_enumerada), '\n')
# print(next(lista_enumerada))   # StopIteration

for item in enumerate(lista):
	print(item)
print('')

for item in enumerate(lista):
	indice, nome = item
	print(indice, nome)
print('')

for indice, nome in enumerate(lista):
	print(indice, nome, lista[indice])
print('')

for tupla_enumerada in enumerate(lista):
	print('FOR da tupla:')
	for valor in tupla_enumerada:
		print(f'\t{valor}')   # \t = TAB
	