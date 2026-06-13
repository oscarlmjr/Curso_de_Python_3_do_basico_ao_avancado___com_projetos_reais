"""
Funções (def) em Python - *args **kwargs - (Parte 3)
"""

def func(*args, **kwargs):
	print(args)

	nome = kwargs.get('nome')
	idade = kwargs.get('idade')
	print(nome)
	print(idade)

lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]

func(*lista, *lista2, nome='Luiz', sobrenome='Miranda')
