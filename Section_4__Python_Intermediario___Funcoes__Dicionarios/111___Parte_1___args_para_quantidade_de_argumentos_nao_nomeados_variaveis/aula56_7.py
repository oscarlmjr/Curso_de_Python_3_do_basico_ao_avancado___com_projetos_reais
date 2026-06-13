"""
Funções (def) em Python - *args **kwargs - (Parte 3)
"""

def func(*args):
	print(args)

lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]

func(*lista, 10, 20, 30, 40, 50)
func(*lista, *lista2)
