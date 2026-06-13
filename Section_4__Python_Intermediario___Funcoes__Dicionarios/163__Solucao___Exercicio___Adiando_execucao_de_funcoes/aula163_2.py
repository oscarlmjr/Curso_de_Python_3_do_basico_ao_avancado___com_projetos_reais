
# def soma(x, y):
#	 return x + y

# def multiplicacao(x, y):
#	 return x * y

# def executa(funcao, *args):
#	 if funcao == soma:
#		 return funcao(*args, 10)
#	 else:
#		 return funcao(*args, 10)


# soma_com_cinco = executa(soma, 5)
# multiplica_por_dez = executa(multiplicacao, 10)

# print(soma_com_cinco)
# print(multiplica_por_dez)

#################################

def soma(x, y):	
	print(f'x + y = {x + y}')
	return multiplicacao(x, y)


def multiplicacao(x, y):
	return f'x * y = {x * y}'


def adia_execucao(funcao, x):
	if funcao == soma:
		global y
		y = x
	elif funcao == multiplicacao:
		return soma(x, y=y)

adia_execucao(soma, 5)
print(adia_execucao(multiplicacao, 2))

#################################

# def soma(x):	
#	 yield f'x + y = {x + y}'


# def multiplicacao(x):
#	 yield from soma(x)
#	 print(f'x * y = {x * y}')


# lista = [5, 2]

# x, y = lista

# s = multiplicacao(x)

# for n in s:
#	 print(n)

