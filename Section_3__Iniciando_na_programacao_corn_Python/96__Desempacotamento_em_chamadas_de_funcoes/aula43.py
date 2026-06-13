"""
Desempacotamento de listas em Python
"""
lista = ['Luiz', 'João', 'Maria', 1, 2, 3, 4,
		 5, 6, 7, 8, 9, 100]

n1, n2, n3, *outra_lista, ultimo_lista = lista

print(n1, n2, outra_lista, ultimo_lista)
print(n3, outra_lista)
