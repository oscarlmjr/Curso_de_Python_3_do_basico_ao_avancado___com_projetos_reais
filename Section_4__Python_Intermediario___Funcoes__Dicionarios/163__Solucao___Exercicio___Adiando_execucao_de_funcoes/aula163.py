
def soma(x, y):   # assinatura da função
	return x + y

def multiplica(x, y):
	return x * y

def executa(funcao, *args):
	def interna(y):   # closure
		return funcao(*args, y)
	return interna


soma_com_cinco = executa(soma, 5)
multiplica_por_dez = executa(multiplica, 10)

print(soma_com_cinco(10))
print(multiplica_por_dez(10))
