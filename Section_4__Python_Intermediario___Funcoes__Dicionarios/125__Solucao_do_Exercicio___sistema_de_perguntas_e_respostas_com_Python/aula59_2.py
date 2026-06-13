"""
2 - Crie uma funcao1 que recebe uma funcao2 como parâmetro e retorne o
valor da funcao2 executada. Faça a funcao1 executar duas funções que
recebam um número diferente de argumentos.
"""
def mestre(funcao, *args, **kwargs):
	return funcao(*args, **kwargs)

def fala_oi(nome):
	return f'Oi, {nome}!'

def saudacao(nome, saudacao):
	return f'{saudacao}, {nome}!'

executando = fala_oi(nome='Luis')
executando2 = saudacao(saudacao='Bom dia', nome='Luis')
print(executando)
print(executando2)
