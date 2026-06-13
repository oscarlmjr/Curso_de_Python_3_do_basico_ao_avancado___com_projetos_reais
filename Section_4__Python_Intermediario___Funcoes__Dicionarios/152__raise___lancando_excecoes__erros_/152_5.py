
def divide(n, d):
	if d == 0:
		raise ZeroDivisionError('Você está tentando '
								'dividir por zero')

	return n / d


print(divide(8, 0))
