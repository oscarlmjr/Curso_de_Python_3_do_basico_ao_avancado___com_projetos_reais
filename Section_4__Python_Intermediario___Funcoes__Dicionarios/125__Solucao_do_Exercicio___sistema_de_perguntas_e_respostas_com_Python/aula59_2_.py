# 2 - Crie uma funcao1 que recebe uma funcao2 como parâmetro e
# retorne o valor da funcao2 executada. Faça a funcao1 executar
# duas funções que recebam um número diferente de argumentos.

def func1(par_1):
	return par_1

def func2(par_2):
	return par_2

def func3(par_3, par_4):
	print(par_3, par_4)

func1(func2(func3(3, 4)))


def func1(par_1, par_2):
	return par_1, par_2

def func2(par_3):
	print(par_3)

def func3(par_4, par_5):
	print(par_4, par_5)

func1(func2(3), func3(4, 5))


# def funcao1(funcao2, funcao3):
#	 return funcao2, funcao3
#
# def funcao2(a1, a2):
#	 print(a1, a2)
#
# funcao2(1, 2)
#
# def funcao3(a3, a4):
#	 print(a3, a4)
#
# funcao3(3, 4)
