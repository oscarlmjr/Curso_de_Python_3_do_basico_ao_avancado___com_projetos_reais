
def nao_aceito_zero(d):
	if d == 0:
		raise ZeroDivisionError('Você está tentando '
								'dividir por zero')
	# return True


def divide(n, d):
	if not isinstance(n, (float, int)):
		raise TypeError(f'{n} deve ser int ou float.')

	if not isinstance(d, (float, int)):
		raise TypeError(f'{d} deve ser int ou float.')

	nao_aceito_zero(d)

	return n / d


print(divide(8, '0'))
print(divide(8, 2))
