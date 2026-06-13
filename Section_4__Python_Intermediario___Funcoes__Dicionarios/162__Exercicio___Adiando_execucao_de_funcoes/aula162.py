# Exercício - Adiando execução de funções


def soma(parcela1, parcela2):
		return parcela1 + parcela2

def multiplicacao(multiplicando, multiplicador):
		return multiplicando * multiplicador


def criar_funcao(funcao):
	def executa(*args):
		return funcao(*args)
	return executa



soma_com_cinco = criar_funcao(soma)
multiplica_por_dez = criar_funcao(multiplicacao)

print(soma_com_cinco(6, 5))
print(multiplica_por_dez(10, 2))
