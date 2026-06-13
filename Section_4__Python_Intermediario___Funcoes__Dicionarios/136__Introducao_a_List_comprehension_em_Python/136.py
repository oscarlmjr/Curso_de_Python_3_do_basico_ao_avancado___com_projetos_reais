# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.

print(list(range(10)), '\n')

lista = list(range(10))
print(lista, '\n')

lista = []

for numero in range(10):
	lista.append(numero)

print(lista, '\n')

lista = [1 for numero in range(10)]
print(lista, '\n')

lista = [numero for numero in range(10)]
print(lista, '\n')

lista = [numero * 2 for numero in range(10)]
print(lista, '\n')
