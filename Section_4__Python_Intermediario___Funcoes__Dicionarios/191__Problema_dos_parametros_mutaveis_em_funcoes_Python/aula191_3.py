# Problema dos parâmetros mutáveis em funções Python

def adiciona_clientes(nome, lista=None):
	if lista is None:
		lista = []
	lista.append(nome)
	return lista

lista1 = []
cliente1 = adiciona_clientes('Luiz', lista1)
adiciona_clientes('Joana', cliente1)
print(cliente1)
print(lista1, '\n')

cliente2 = adiciona_clientes('Helena')
adiciona_clientes('Maria', cliente2)
print(cliente2)
print(lista1, '\n')
