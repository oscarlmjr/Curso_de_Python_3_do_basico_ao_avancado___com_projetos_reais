# Split, Join, Enumerate em Python
# * Split - Dividir uma string # str
# * Join - Juntar uma lista # str
# * Enumerate - Enumerar elementos da lista
# # list / iteráveis

string = 'o Brasil é penta, o Brasil é penta,'
lista_1 = string.split(' ')
lista_2 = string.split(',')
for valor in lista_1:
	print(f'A palavra "{valor}" apareceu \n'
		  f'{lista_1.count(valor)}x na frase.')
print('')
for valor in lista_2:
	print(f'A - palavra "{valor}" apareceu \n'
		  f'{lista_2.count(valor)}x na frase.')  # "" ?
