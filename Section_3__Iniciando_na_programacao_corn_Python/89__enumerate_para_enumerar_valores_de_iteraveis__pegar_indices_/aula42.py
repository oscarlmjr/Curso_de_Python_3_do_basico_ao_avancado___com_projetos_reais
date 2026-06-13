"""
* Enumerate - Enumerar elementos da lista
# list
"""
lista = [
	['Edu', 'João', 'Luiz'],
	['Maria', 'Aline', 'Joana'],
	['Helena', 'Ed', 'Lu']
]
print(lista[1][2])
enumerada = enumerate(lista)
print(enumerada)
print(list(enumerada))
enumerada = list(enumerate(lista))
print(enumerada)
print(enumerada[1][0])
print(enumerada[1][1])
print(enumerada[1][1][2])
