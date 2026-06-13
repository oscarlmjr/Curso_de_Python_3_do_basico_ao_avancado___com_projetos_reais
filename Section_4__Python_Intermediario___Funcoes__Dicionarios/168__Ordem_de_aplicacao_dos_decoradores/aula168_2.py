# Ordem dos decoradores

def parametros_decorador(nome):
	print(f'parametros_decorador: {nome=}')

	def decorador(func):
		print(f'{nome=}')
		print(func.__name__, type(func), nome, type(nome))

		def sua_nova_funcao(*args):
			print(func.__name__, *args)
			res = func(*args)
			final = f'{res} {nome}'
			return final

		return sua_nova_funcao

	return decorador

@parametros_decorador(nome='3')
@parametros_decorador(nome='2')
@parametros_decorador(nome='1')

def soma(x, y):
	return x + y

dez_mais_cinco = soma(10, 5)
print(dez_mais_cinco)
