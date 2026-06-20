"""
* Enumerate - Enumerar elementos da lista
# list
"""
lista = [
	['Edu', 'João', 'Luiz'],
	['Maria', 'Aline', 'Joana'],
	['Helena', 'Ed', 'Lu'],
]
for v1, v2 in enumerate(lista, 53):
	print(v1, v2)

for v1 in enumerate(lista, 53):
	print(v1)

for v1 in enumerate(lista):
	print(v1)
