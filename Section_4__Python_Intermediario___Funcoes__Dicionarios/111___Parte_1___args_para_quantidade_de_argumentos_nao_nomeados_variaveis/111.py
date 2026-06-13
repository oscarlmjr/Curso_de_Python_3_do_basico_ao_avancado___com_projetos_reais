'''
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
'''
# Desempacotamento

x, y, *resto = 1, 2, 3, 4
print(x, y, resto)
print(x, y, *resto, '\n')


def soma(*args):
	print(args, type(args))
	print(*args, '\n')
	for numero in args:
		print(numero)
	print('')
	args = list(args)
	print(args, type(args))
	print(*args, '\n')


soma(1, 2, 3, 4, 5, 6)
