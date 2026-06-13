
def multiplicar(*args):
	total = 1   # multiplicação por 0 é igual a 0
	for numero in args:
		total *= numero
	return total


multiplicação = multiplicar(10, 2, 3, 4, 5)   # variavel aceita acentuação
print(multiplicação)
