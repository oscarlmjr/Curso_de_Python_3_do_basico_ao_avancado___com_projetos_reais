# Problema dos parâmetros mutáveis em funções Python

def adiciona_clientes(nome, lista=[]):
	lista.append(nome)
	return lista


cliente1 = adiciona_clientes('Luiz')
adiciona_clientes('Joana', cliente1)
# adiciona_clientes('Joana')
print(cliente1)

cliente2 = adiciona_clientes('Helena')
adiciona_clientes('Maria', cliente2)
# adiciona_clientes('Maria')
print(cliente2)
