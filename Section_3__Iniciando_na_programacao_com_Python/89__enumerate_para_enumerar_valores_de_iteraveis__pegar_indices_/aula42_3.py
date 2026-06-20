"""
* Enumerate - Enumerar elementos da lista # list
"""
lista = [
	['Edu', 'João', 'Luiz'],
	['Maria', 'Aline', 'Joana'],
	['Helena', 'Ed', 'Lu'],
]
for v1 in enumerate(lista, 53):
	valor_enumerado, minha_lista = v1
	print(valor_enumerado, minha_lista)

for v1 in enumerate(lista, 53):
	valor_enumerado, minha_lista = v1
	nome1, nome2, nome3 = minha_lista
	print(nome1, nome3)
