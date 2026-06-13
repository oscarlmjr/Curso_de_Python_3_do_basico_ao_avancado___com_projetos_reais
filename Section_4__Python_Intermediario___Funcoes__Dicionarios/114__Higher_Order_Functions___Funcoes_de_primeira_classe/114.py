'''
Higher Order Functions
Funções de primeira classe
'''
def saudacao(msg):
	return f'{msg}'

def executa(funcao):
	return funcao('Bom dia, Luiz')

print(executa(saudacao))


def saudacao(msg, nome):
	return f'{msg}, {nome}'

def executa(funcao, *args):
	return funcao(*args)

print(
	executa(saudacao, 'Bom dia', 'Luiz')
)
