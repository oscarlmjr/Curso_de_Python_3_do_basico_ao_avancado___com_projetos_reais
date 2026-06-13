"""
Funções (def) em Python - *args **kwargs - (Parte 3)
"""

def func(*args):
	args = list(args)
	args[0] = 20
	print(args)

func(1,2,3,4,5)

def func(*args):
	for v in args:
		print(v)

func(1,2,3,4,5)
