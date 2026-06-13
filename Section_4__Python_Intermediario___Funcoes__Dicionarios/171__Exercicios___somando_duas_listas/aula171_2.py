"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a	 = [1, 2, 3, 4, 5, 6, 7]
lista_b	 = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""
from itertools import zip_longest


lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]
lista_c = []

for n in list(zip(lista_a, lista_b)):
	x, y = n
	lista_c.append(x + y)

print(lista_c)
# print(Lista_a + lista_b)

###########################

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]
lista_soma = []

for n in range(min(len(lista_a), len(lista_b))):
	lista_soma.append(lista_a[n] + lista_b[n])

print(lista_soma)

###########################

lista_soma = []

def tamanho_a(x):
	def tamanho_b(y):
		return min(x, y)
	return tamanho_b

tamanho_lista = tamanho_a(len(lista_a))

for n in range(tamanho_lista(len(lista_b))):
	lista_soma.append(lista_a[n] + lista_b[n])

print(lista_soma)
