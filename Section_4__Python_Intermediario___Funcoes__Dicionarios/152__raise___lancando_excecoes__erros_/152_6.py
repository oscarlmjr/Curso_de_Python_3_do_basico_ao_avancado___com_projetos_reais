
def nao_aceito_zero(d):
	if d == 0:
		raise ZeroDivisionError('Você está tentando '
								'dividir por zero')


def divide(n, d):
	nao_aceito_zero(d)
	
	return n / d


print(divide(8, 0))
print(divide(8, 2))
