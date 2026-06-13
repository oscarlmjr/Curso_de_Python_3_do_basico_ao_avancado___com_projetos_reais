
def executa(funcao, *args):
	return funcao(*args)


def soma(x, y):
	return x + y


def cria_multiplicador(multiplicador):
	def multiplica(numero):
		return f'cria_multiplicador(multiplicador) = {multiplicador} '\
			   f' *  multiplica(numero) = duplica({numero}) = ' \
			   f'{numero * multiplicador}\n'
	return multiplica


duplica = cria_multiplicador(2)
print(duplica(3))

# funcao = lambda parametro: parametro   # má prática

print(executa(lambda x, y: x + y, 2, 3),
	  executa(soma, 2, 3),
	  soma(2, 3))
	