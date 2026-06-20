"""
Split, Join, Enumerate em Python
* Split - Dividir uma string # str
* Join - Juntar uma lista # str
* Enumerate - Enumerar elementos da lista
# list / iteráveis
"""
lista = [[1, 2], [3, 4], [5, 6]]
for v in lista:
	print(v)
for v in lista:
	print(v[0], v[1])
lista = [[1, 4, 'Luiz'], [1, 5, 'João'], [3, 6, 'Maria']]
for indice, valor, nome in lista:
	 print(valor, indice, nome)
lista = ['Luiz', 'João', 'Maria']
for indice, nome in enumerate(lista):
	print(indice, nome)
lista = ['Luiz', 'João', 'Maria']
n1, n2, n3 = lista
# lista = n1, n2, n3 = lista
print(n2)
