"""
Split, Join, Enumerate em Python
* Split - Dividir uma string # str
* Join - Juntar uma lista # str
* Enumerate - Enumerar elementos da lista
# list / iteráveis
"""
string = 'O Brasil é o país do futebol, ' \
	'o Brasil é penta.'
lista_1 = string.split(' ')
lista_2 = string.split(',')
# .strip() retira espaço no começo e fim do elemento
for valor in lista_2:
	print(valor.strip().capitalize())
string = 'O Brasil é penta.'
lista = string.split(' ')
string2 = ','.join(lista)
print(string)
print(lista)
print(string2)
