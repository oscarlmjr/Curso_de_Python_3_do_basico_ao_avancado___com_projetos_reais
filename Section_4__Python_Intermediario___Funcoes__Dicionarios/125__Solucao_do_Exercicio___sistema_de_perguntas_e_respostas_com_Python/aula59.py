"""
1 - Crie uma funcao1 que receba uma funcao2 como parâmetro e retorne
o valor da funcao2 executada.
"""
def ola_mundo():
	return 'Olá Mundo!'

def mestre(funcao):
	return funcao()

executando = mestre(ola_mundo)
print(executando)
