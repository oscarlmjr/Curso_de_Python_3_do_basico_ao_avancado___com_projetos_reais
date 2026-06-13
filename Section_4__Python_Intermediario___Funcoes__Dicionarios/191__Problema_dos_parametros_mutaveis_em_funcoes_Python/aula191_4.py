# Problema dos parâmetros mutáveis em funções Python

def adiciona_clientes(nome, lista=None):
	if lista is None:
		lista = []
	lista.append(nome)
	return lista

cliente1 = adiciona_clientes('Luiz')
adiciona_clientes('Joana', cliente1)
adiciona_clientes('Fernando', cliente1)
cliente1.append('Edu')
print(cliente1, '\n')

cliente2 = adiciona_clientes('Helena')
adiciona_clientes('Maria', cliente2)
print(cliente2, '\n')

lista2 = []
cliente3 = adiciona_clientes('Moreira', lista2)
adiciona_clientes('Vivi', cliente3)
print(cliente3, lista2, '\n')
