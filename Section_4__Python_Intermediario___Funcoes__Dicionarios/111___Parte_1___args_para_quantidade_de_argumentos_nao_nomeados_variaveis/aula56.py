"""
Funções (def) em Python - *args **kwargs - (Parte 3)
"""

def func(a1, a2, a3, a4, a5, nome=None, a6=None):
	print(a1, a2, a3, a4, a5, nome, a6)
	return nome, a6

func(1, 2, 3, 4, 5, nome='Luiz', a6='5')
var = func(1, 2, 3, 4, 5, nome='Luiz', a6='6')
print(var)
print(func(1, 2, 3, 4, 5, nome='Luiz', a6='7'))
func(1, 2, 3, 4, 5, nome='Luiz', a6='5')
print(var[0], var[1])
