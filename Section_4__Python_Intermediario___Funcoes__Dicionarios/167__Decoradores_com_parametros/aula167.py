# Decoradores com parâmetros
def decoradora(func):
	print(func.__name__, type(func))

	def aninhada(*args):
		print(func.__name__, type(func), *args, type(args))
		res = func(*args)
		return res
	return aninhada

@decoradora
def soma(x, y):
	return x + y

dez_mais_cinco = soma(10, 5)

print(dez_mais_cinco)
