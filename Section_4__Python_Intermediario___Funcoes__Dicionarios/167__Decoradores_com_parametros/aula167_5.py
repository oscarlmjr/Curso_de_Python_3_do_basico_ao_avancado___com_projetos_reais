# Decoradores com parâmetros
def fabrica_de_funcoes(func):
	print(func.__name__, type(func))

	def aninhada(*args):
		print(func.__name__, type(func), *args, type(args))
		res = func(*args)
		return res
	return aninhada

def fabrica_de_decoradores(a, b, c):
	return fabrica_de_funcoes

@fabrica_de_decoradores(1, 2, 3)
def soma(x, y):
	return x + y

multiplica = fabrica_de_funcoes(lambda x, y: x * y)

dez_mais_cinco = soma(10, 5)
nove_vezes_quatro = multiplica(9, 4)

print(dez_mais_cinco)
print(nove_vezes_quatro)
