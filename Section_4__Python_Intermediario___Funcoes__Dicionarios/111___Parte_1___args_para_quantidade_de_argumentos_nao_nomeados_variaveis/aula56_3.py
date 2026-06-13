"""
Funções (def) em Python - *args **kwargs - (Parte 3)
"""

def func(*args):
	print(args)
	print(*args)
	print(args[0])
	print(args[-1])
	print(len(args))

func(1, 2, 3, 4, 5)
