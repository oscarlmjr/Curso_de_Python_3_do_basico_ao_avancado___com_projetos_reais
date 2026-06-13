
def executa(funcao, *args):
	print('args = ', args)
	return funcao(*args)


def soma(x, y):
	return x + y


duplica = executa(lambda m: lambda n: n * m, 2)
print(duplica(3), '\n')


print(
	f'{executa(lambda x, y: x + y, 2, 3)}, '
	f'{executa(soma, 2, 3)}, {soma(2, 3)}, '
	f'{executa(lambda *args: sum(args), 1, 2, 3, 4, 5, 6, 7)} \n'
)
